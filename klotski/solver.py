from .board import *
import copy
import time
import itertools

CARDINAL_MOVE_VECTORS = {Vector2(0, 1), Vector2(0, -1), Vector2(1, 0), Vector2(-1, 0)}

"""
The Plan™

Start
- start with move depth 0, a list of a single path object (the current board state + the moves to get there)
- also start with a set of hashes. this is to keep track of unique board states

Loop
- make every move possible (every block + position) from all the paths in move depth N
--- never move the # (immovable) "block"
--- do it by using the cardinal moves to find every position, using similar recursion.
--- don't try to move the previously moved block. we already moved it
*-- if the board is in a solved state (all goal blocks are in goal positions), we are done (return solution path)
- save those (the move made and the new board state) to a move depth N+1 list, but only if the board state is unique.
--- only verify the board's uniqueness *after* making every move possible with a block. you might cut off a path to new moves early
--- probably best to calculate all moves first
*-- if move depth exceeds maximum moves or the move depth list is empty, then we can stop (no solution found)

Finish
- if we got a successful solution, use the solution path to generate a full solution
--- probably print it to a file tbh
- if we didn't get a successful solution, mention the failure (exceeded maximum move depth, or got stuck)

Fun Stuff
- might be interesting to print how long the program takes to explore each move depth? and how many moves there were to explore
--- include the time to explore too
"""


# Represents a potential path to the solution.
class SolutionPath:
    # current_board is a Board representing the current state of the puzzle
    # move_history is a list of Moves to go from the initial board to this one
    def __init__(self, current_board, move_history):
        self.current_board = current_board
        self.move_history = move_history
    
    # get cid of last moved block (returns None if no moves have been made yet)
    def last_moved_block(self):
        if self.move_history:
            return self.move_history[len(self.move_history) - 1].cid
    
    def solution_length(self):
        return len(self.move_history)


# Generates a list of all possible paths one move deeper via moving block cid.
def _generate_all_block_moves(path, cid):
    all_block_move_paths = []
    used_move_vectors = {Vector2(0, 0)} # hack: we obviously don't want "didn't move the piece" to be a move
    active_move_vectors = [Vector2(0, 0)]
    
    while active_move_vectors:
        new_active_move_vectors = []
        # tries moving one step UDLR in each direction
        potential_new_move_vectors = list(map(lambda i: i[0] + i[1], itertools.product(active_move_vectors, CARDINAL_MOVE_VECTORS))) # baby's first itertools usage
        
        for v in potential_new_move_vectors:
            if v not in used_move_vectors:
                used_move_vectors.add(v) # if haven't made this move before, add it so we don't try it again
                new_move = Move(cid, v)
                new_board = path.current_board.shifted_by(new_move)
                if new_board is not None: # if the move is valid, add it to the list of move paths
                    new_path = copy.deepcopy(path)
                    new_path.current_board = new_board
                    new_path.move_history.append(new_move)
                    all_block_move_paths.append(new_path)
                    new_active_move_vectors.append(v) # try moving UDLR from here next time
        
        active_move_vectors = new_active_move_vectors
    
    return all_block_move_paths


# Generates all possible new paths one move deeper from a list of solution paths
# Doesn't check if the board positions are unique.
def _generate_new_paths(paths):
    if not paths: return []
    
    all_new_paths = [] # new ones from every single path in paths
    all_block_cids = set(paths[0].current_board.blocks.keys())
    all_block_cids.discard(IMMOVABLE)
    
    for path in paths:
        new_paths = [] # new ones from the current path we're checking
        blocks_to_move = copy.copy(all_block_cids)
        blocks_to_move.discard(path.last_moved_block())
        
        for cid in blocks_to_move:
            all_new_paths = all_new_paths + _generate_all_block_moves(path, cid)
    
    return all_new_paths


# Returns a SolutionPath that led to the solution, or returns None if failed
# (whether by exceeding max search depth or by getting stuck)
def find_solution(board, goal, max_search_depth, verbose = False):
    current_paths = [SolutionPath(board, [])]
    explored_board_positions = {board.board_hash(goal)}
    t0 = time.time()
    t1 = time.time()
    
    for i in range(max_search_depth): # current search depth = i + 1
        potential_new_paths = _generate_new_paths(current_paths)
        
        # verify board uniqueness
        new_paths = []
        for path in potential_new_paths:
            board_hash = path.current_board.board_hash(goal)
            if board_hash not in explored_board_positions:
                explored_board_positions.add(board_hash)
                new_paths.append(path)
                
                # also verify the solution while we're at it
                if goal.is_fulfilled(path.current_board):
                    return path
        
        if not new_paths:
            print("Can't reach the goal state from this board configuration")
            return None
        
        current_paths = new_paths
        
        if verbose:
            t1 = time.time()
            print("Searched solution depth {0} ({1} possible paths, took {2} seconds)".format(i + 1, len(current_paths), t1 - t0))
            t0 = t1
            
        
    print("Couldn't find a solution within {} moves".format(max_search_depth))
    return None
