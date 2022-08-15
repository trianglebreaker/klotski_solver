from .board import *
import time

CARDINAL_MOVE_DIRECTIONS = {Vector2(0, 1), Vector2(0, -1), Vector2(1, 0), Vector2(-1, 0)}

"""
The Plan™

Start
- start with move depth 0, a list of a single path object (the current board state + the moves to get there)
- also start with a set of hashes. this is to keep track of unique board states

Recursion Loop
- make every move possible (every block + position) from all the paths in move depth N
--- move solution blocks first, and never move the # (immovable) "block"
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


