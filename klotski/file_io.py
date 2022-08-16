from .constants import *
from .solver import *
import re

# Reads a text file for sliding puzzle data.
# Returns a list containing all the boards in the board string format.
def read_board_strings_from_file(path):
    boards = []
    p1 = re.compile("^[^$]*") # match up to but not including the first $
    p2 = re.compile("[\s]") # match any whitespace
    
    with open(path, mode = "r") as file:
        current_board = []
        
        def push_board():
            nonlocal current_board
            if current_board:
                boards.append(current_board)
            current_board = []
        
        while True:
            line = file.readline()
            if line == "":                      # break when EOF
                push_board()
                break
            line = re.search(p1, line)[0]       # remove comments
            line = re.sub(p2, "", line)         # remove whitespace
            if line == "": continue             # skip empty lines
            
            if line[0] == NEW_BOARD:
                push_board()
            else:
                current_board.append(line)
    
    return boards


# Writes the step-by-step solution to a text file.
def write_solution_to_file(path, solution_path, initial_board):
    with open(path, mode = "w") as file:
        current_board = initial_board
        
        file.write("====================\nInitial board state\n====================\n\n")
        file.write(initial_board.pretty_string() + "\n\n")
        file.write("====================\nSolution ({} moves)\n====================\n".format(len(solution_path.move_history)))
        
        for i, move in enumerate(solution_path.move_history):
            file.write("\nStep {0}: Move block {1}\n\n".format(i + 1, move.cid))
            current_board = current_board.shifted_by(move)
            file.write(current_board.pretty_string())
            file.write("\n")
