import klotski.board as board

coord1 = board.Coordinate(1, 2)
coord2 = board.Coordinate(2, 2)
set1 = {coord1, coord2}
coord2.x = 3

block = board.Block.from_cells([board.Coordinate(0, 0), board.Coordinate(0, 1), board.Coordinate(1, 1)])


# "#" represents an immovable block (useful for modeling non-rectangular boards)
# "." represents an empty space where blocks can move to
# the start configuration includes all blocks at the start. each character is a unique block
# the goal configuration should only show where the goal block(s) need(s) to go, the rest is empty

start = [
    "AA.",
    ".BC",
    ".DC",
    ]

goal = [
    "...",
    ".AA",
    ]

b = board.Board.from_string_list_form(start)
print(b)
print(b.pretty_board_string())
