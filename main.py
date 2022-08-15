import klotski.solver as b

"""
block = b.Block("a", {b.Vector2(0, 0), b.Vector2(0, 1), b.Vector2(1, 1)})
print(block)
print(block.shifted_by(b.Vector2(1, 1)))
print(block)
"""

# "#" represents an immovable block (useful for modeling non-rectangular boards)
# "." represents an empty space where blocks can move to
# the start configuration includes all blocks at the start. each character is a unique block
# the goal configuration should only show where the goal block(s) need(s) to go, the rest is empty

start = [
    "AACCF",
    "!!EG.",
    "!!EH.",
    "BBDDI",
    ]

goal = [
    ".....",
    "...!!",
    "...!!",
    ".....",
    ]

board = b.create_board_from_board_strings(start, goal)
print(board.pretty_string())
print("")
print(board.shifted_by(b.Move("F", b.Vector2(0, 2))).pretty_string())

print("")
print(board.shifted_by(b.Move("F", b.Vector2(0, 3))))

