import sys
import time
from os import path
import klotski

MAX_SEARCH_DEPTH = 200
PRINT_VERBOSE = True

def print_and_quit(message):
    print(message)
    quit()


def main():
    filepath = None
    solution_filepath = None
    board = None
    goal = None
    solution_path = None
    
    if not (__name__ == "__main__"): print_and_quit("Run this as a script please")
    
    # Verify file path and prepare solution path
    if len(sys.argv) > 3: print_and_quit("Too many arguments; provide only 1 filepath")
    if len(sys.argv) >= 2:
        filepath = sys.argv[1]
    else:
        print("Please provide the file path to a puzzle (e.g. \"./examples/queens_escape.txt\"):")
        filepath = input()
    
    if not (path.isfile(filepath) and filepath[-4:] == ".txt"): print_and_quit("Path must point to an existing .txt file")
    
    solution_filepath = filepath[0:(len(filepath) - 4)] + "_solution.txt"
    
    # Load and solve puzzle (and provide time output)
    t0 = time.time()
    
    board_strings = klotski.read_board_strings_from_file(filepath)
    if len(board_strings) < 2: print_and_quit("Puzzle file must specify the starting setup and the goal pieces' positions")
    board = klotski.board_from_board_string(board_strings[0])
    goal = klotski.goal_from_board_string(board_strings[1])
    
    if not goal.blocks: print_and_quit("No goal blocks (did you forget to add blocks to the goal board?)")
    
    if not goal.is_feasible(board): quit()
    
    t1 = time.time()
    print("Successfully loaded puzzle (took {} seconds)".format(t1 - t0))
    
    # Solve puzzle
    solution_path = klotski.find_solution(board, goal, MAX_SEARCH_DEPTH, verbose = PRINT_VERBOSE)
    if solution_path is None: quit()
    
    t2 = time.time()
    print("Found a solution of length {1} moves (took {0} seconds). Saving solution...".format(t2 - t1, solution_path.solution_length()))
    
    # writing solution to file goes here
    
    print("Solution saved to {}".format(solution_filepath))


main()

