from .constants import *

# A single coordinate on the board. Could mean a square, or a position.
class Coordinate:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def shifted(self, dx, dy):
        return Coordinate(self.x + dx, self.y + dy)
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


# A block to be moved around. Consists of a shape and position (ul).
class Block:
    # cells is a list of all coords making up the block
    def __init__(self, shape, ul, br):
        self.shape = shape
        self.ul = ul
        self.br = br
    
    @classmethod
    def from_cells(cls, cells):
        xx = set(map(lambda i: i.x, cells))
        yy = set(map(lambda i: i.y, cells))
        ul = Coordinate(min(xx), min(yy))
        br = Coordinate(max(xx), max(yy))
        shape = set(map(lambda i: i.shifted(ul.x * -1, ul.y * -1), cells))
        return cls(shape, ul, br)
    
    def shifted(self, dx, dy):
        return Block(shape, ul.shifted(dx, dy), br.shifted(dx, dy))
    
    def __str__(self):
        line_c = "Corners: " + str(self.ul) + ", " + str(self.br)
        line_s = []
        for c in self.shape:
            line_s.append(str(c))
        return "Shape: [" + ", ".join(line_s) + "]\n" + line_c


# Represented via board dimensions and a dictionary of block ids to block objects.
class Board:
    # length and height are the horizontal + vertical dimensions of the board
    # blocks is a dict of block uids to block objects. assumes none overlap
    def __init__(self, length, height, blocks):
        self.length = length
        self.height = height
        self.blocks = blocks
    
    @classmethod
    # string_list is a list of strings used to denote the board
    # each string is a row, each character is a (part of a) block
    # all strings must be the same length or else this goes boom
    # if you want irregular boards, fill them in with # chars
    def from_string_list_form(cls, string_list):
        length = len(string_list[0])
        height = len(string_list)
        blocks_as_cells = {}
        
        for y, row in enumerate(string_list):
            if (len(row) != length):
                raise AssertionError("Board strings are of unequal length (use \"" + IMMOVABLE + "\" for solid immovable cells)")
            for x, char in enumerate(string_list[y]):
                if char == EMPTY: continue
                if char not in blocks_as_cells:
                    blocks_as_cells[char] = {Coordinate(x, y)}
                else:
                    n = blocks_as_cells[char] # doesn't work on one line for some reason???
                    blocks_as_cells[char].add(Coordinate(x, y))
        
        blocks = {}
        for uid, cells in blocks_as_cells.items():
            blocks[uid] = Block.from_cells(cells)
        
        return cls(length, height, blocks)
    
    def __str__(self):
        header = "Board size: " + str(self.length) + " wide, " + str(self.height) + " high\n\n"  
        body = []
        for uid, block in self.blocks.items():
            item = "* Block " + uid + ":\n" + str(block)
            body.append(item)
        return header + "\n\n".join(body)
    
    def pretty_board_string(self):
        string_list_list = []
        for _ in range(self.height):
            row = []
            for _ in range(self.length):
                row.append(EMPTY)
            string_list_list.append(row)
        for uid, block in self.blocks.items():
            for c in block.shape:
                string_list_list[c.y + block.ul.y][c.x + block.ul.x] = uid
        for i, string_list in enumerate(string_list_list):
            string_list_list[i] = "".join(string_list)
        return "\n".join(string_list_list)
