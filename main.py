import klotski

"""
block = b.Block("a", {b.Vector2(0, 0), b.Vector2(0, 1), b.Vector2(1, 1)})
print(block)
print(block.shifted_by(b.Vector2(1, 1)))
print(block)
"""

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

print(klotski.read_board_strings_from_file("./examples/diabolical_box.txt"))

