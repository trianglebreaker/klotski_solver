from .constants import *
import functools
import copy

# A set of two numbers.
class Vector2:
    # x and y are numbers (preferably integers)
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


# A single block in the sliding puzzle.
# Consists of the block's single-character ID and the cells that make up the block.
class Block:
    # cid is a single-character string
    # cells is a set of Vector2s
    def __init__(self, cid, cells):
        self.cid = cid
        self.cells = cells
        xx = set(map(lambda i: i.x, cells))
        yy = set(map(lambda i: i.y, cells))
        self.position = Vector2(min(xx), min(yy))
        self.size = Vector2(max(xx) - min(xx) + 1, max(yy) - min(yy) + 1)
    
    # returns a new block.
    # delta is a Vector2 that shifts the block
    def shifted_by(self, delta):
        return Block(self.cid, set(map(lambda i: i + delta, self.cells)))
    
    # anonymous_hash creates a hash of the block that doesn't take its cid into account.
    # Thus, two blocks with the same shape and position should give the same hash.
    # This lets us combine identical configurations of non-goal blocks (eg. AB and BA)
    # and save on search time.
    # https://alaraph.com/2021/09/10/solving-the-klotski-puzzle-in-scala/
    def anonymous_hash(self):
        # ok first: map will create an iterable with a list of all the hashed Vector2s, using the Vector2 hash function
        # then we turn it into a list so we can sort it, then into a tuple so we can hash it. totally not confusing
        return hash(tuple(sort(list(map(lambda i: hash(i), self.cells)))))
    
    # today I learned onymous is the opposite of anonymous. weird
    def onymous_hash(self):
        return hash((cid, anonymous_hash()))
    
    def __eq__(self, other):
        cell_eq = functools.reduce(lambda i, j: i and j, map(lambda i, j: i.x == j.x and i.y == j.y, self.cells, other.cells))
        cid_eq = self.cid == other.cid
        return cid_eq and cell_eq
    
    def __str__(self):
        return self.cid + ": " + ", ".join(map(lambda i: str(i), self.cells))


# A representation of a single move.
# Consists of block cid and the delta of the move.
class Move:
    def __init__(self, cid, delta):
        self.cid = cid
        self.delta = delta


# A representation of the board and all its blocks (and any immovable tiles).
class Board:
    # dimensions is a Vector2; x is length, y is height
    # blocks is a dict of block ids to Blocks for the current board state
    # goal_blocks is a dict of block ids to Blocks for the goal positions of some blocks
    def __init__(self, dimensions, blocks):
        self.dimensions = dimensions
        self.blocks = blocks
    
    # Takes in a move object, and produces a new board with the move executed.
    # Returns None if the move is invalid (out of bounds, or overlaps a block).
    def shifted_by(self, move):
        shifted_block = self.blocks[move.cid].shifted_by(move.delta)
        # out of bounds check
        if not (0 <= shifted_block.position.x <= self.dimensions.x - shifted_block.size.x and 0 <= shifted_block.position.y <= self.dimensions.y - shifted_block.size.y):
            return None
        # overlap check
        other_blocks = list(filter(lambda i: i.cid != shifted_block.cid, self.blocks.values()))
        other_points = functools.reduce(lambda i, j: i | j, map(lambda i: i.cells, other_blocks))
        if other_points & shifted_block.cells != set():
            return None
        # create new board and shift piece accordingly
        new_board = copy.deepcopy(self)
        new_board.blocks[shifted_block.cid] = shifted_block
        return new_board
    
    def pretty_string(self):
        string_list_list = []
        for _ in range(self.dimensions.y):
            row = []
            for _ in range(self.dimensions.x):
                row.append(EMPTY)
            string_list_list.append(row)
        for cid, block in self.blocks.items():
            for c in block.cells:
                string_list_list[c.y][c.x] = cid
        string_list_list = list(map(lambda i: "".join(i), string_list_list))
        return "\n".join(string_list_list)
    
    # We want indistinguishable board positions to give the same hash, so the goal is needed
    def board_hash(self, goal):
        h = []
        for block in blocks:
            if block.cid in goal.blocks:
                h.append(block.onymous_hash())
            else:
                h.append(block.anonymous_hash())
        return hash(tuple(sort(h)))
    
    def __str__(self):
        header = "Board size: " + str(self.dimensions.x) + " wide, " + str(self.dimensions.y) + " tall"
        blocks = "\n".join(map(lambda i: str(i), self.blocks.values()))
        return header + "\nBlocks:\n" + blocks


# A representation of the goal.
# Consists only of the blocks that need to be in a certain position.
class Goal:
    # blocks is a dict of block ids to Blocks for the end positions of the goal blocks
    def __init__(self, blocks):
        if IMMOVABLE in blocks:
            blocks.pop(IMMOVABLE)
        self.blocks = blocks
    
    # Checks if the goal makes sense for this board (goal blocks exist and are the same shape)
    def is_feasible(self, board):
        for block in self.blocks.values():
            # existence check
            if block.cid not in board.blocks:
                print("Block " + block.cid + " not present on board")
                return False
            # shape check
            board_block = board.blocks[block.cid]
            goal_block_ul_aligned = block.shifted_by(Vector2(-block.position.x, -block.position.y))
            board_block_ul_aligned = board_block.shifted_by(Vector2(-board_block.position.x, -board_block.position.y))
            if goal_block_ul_aligned.cells ^ board_block_ul_aligned.cells != set():
                print("Block " + block.cid + " in goal differently shaped than block " + block.cid + " on board")
                return False
        return True
    
    # Checks if the goal has been met (goal blocks are in the right position)
    # Assumes goal feasibility has already been checked
    def is_fulfilled(self, board):
        pass


def board_string_to_blocks(board_string):
    length = len(board_string[0])
    height = len(board_string)
    cell_groups = {}
    
    for y, row in enumerate(board_string):
        if (len(row) != length):
            raise AssertionError("Board strings are of unequal length (use \"" + IMMOVABLE + "\" for solid immovable cells)")
        for x, cid in enumerate(board_string[y]):
            if cid == EMPTY: continue
            if cid not in cell_groups:
                cell_groups[cid] = {Vector2(x, y)}
            else:
                # can't be one line for some reason
                n = cell_groups[cid]
                n.add(Vector2(x, y))
                cell_groups[cid] = n
    
    blocks = {}
    for cid, cells in cell_groups.items():
        blocks[cid] = Block(cid, cells)
    
    return blocks


def board_from_board_string(board_string):
    dimensions = Vector2(len(board_string[0]), len(board_string))
    blocks = board_string_to_blocks(board_string)
    return Board(dimensions, blocks)


def goal_from_board_string(board_string):
    blocks = board_string_to_blocks(board_string)
    return Goal(blocks)

