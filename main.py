import sys
from os import path
import klotski

MAX_SOLUTION_DEPTH = 200
board = None
goal = None
solution_path = None


def print_and_quit(message):
    print(message)
    quit()


def prepare_puzzle(filepath):
    board_strings = klotski.read_board_strings_from_file(filepath)
    if len(board_strings) < 2: print_and_quit("Puzzle file must specify the starting setup and the goal pieces' positions")
    board = klotski.board_from_board_string(board_strings[0])
    goal = klotski.goal_from_board_string(board_strings[1])
    
    if not goal.blocks: print_and_quit("No goal (did you forget to add blocks in the goal board?)")
    
    if not goal.is_feasible(board): quit()


def solve_puzzle():
    pass


def main():
    if not (__name__ == "__main__"): print_and_quit("Run this as a script please")
        
    if len(sys.argv) > 3: print_and_quit("Too many arguments; provide only 1 filepath")
    filepath = ""
    if len(sys.argv) >= 2:
        filepath = sys.argv[1]
    else:
        print("Please provide the file path to a puzzle (e.g. \"./examples/queens_escape.txt\"):")
        filepath = input()
    
    if not (path.isfile(filepath) and filepath[-4:] == ".txt"): print_and_quit("Path must point to an existing .txt file")
    
    print("filepath valid")
    prepare_puzzle(filepath)
    solve_puzzle()
    

main()







# "#" represents an immovable block (useful for modeling non-rectangular boards)
# "." represents an empty space where blocks can move to
# the start configuration includes all blocks at the start. each character is a unique block
# the goal configuration should only show where the goal block(s) need(s) to go, the rest is empty or immovable

cv_start = [
    "AACCF",
    "!!EG.",
    "!!EH.",
    "BBDDI",
    ]

cv_goal = [
    ".....",
    "...!!",
    "...!!",
    ".....",
    ]

start = [
    "AAB",
    "CD.",
    "#..",
    ]

goal = [
    "...",
    "...",
    ".AA",
    ]



'''
board = klotski.board_from_board_string(start)
print(board.pretty_string())
print("")
print(board.shifted_by(klotski.Move("B", klotski.Vector2(0, 2))).pretty_string())
print("")
print(board.shifted_by(klotski.Move("B", klotski.Vector2(0, 3))))
'''

# print(klotski.read_board_strings_from_file("./examples/example.txt"))

