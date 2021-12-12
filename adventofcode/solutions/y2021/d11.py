'''
Solution for day 11 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 11` from the project root.
'''
from dataclasses import dataclass

from adventofcode.types import Solution


@dataclass(frozen=True, eq=True)
class Point:
    y: int
    x: int

    def is_valid(self, board):
        max_x = len(board[0])
        max_y = len(board)
        if max_x > self.x >= 0 and max_y > self.y >= 0:
            return True
        return False


def flash(pos, board, flashed):
    if not pos.is_valid(board):
        #        print(f"invalid pos: {pos}")
        return
    if pos in flashed:
        return

    board[pos.y][pos.x] += 1
    if board[pos.y][pos.x] > 9:
        flashed.add(pos)
        # print(f"flashing {pos} with value {board[pos.y][pos.x]}")
        for increase_pos in [Point(pos.y - 1, pos.x - 1), Point(pos.y - 1, pos.x), Point(pos.y - 1, pos.x + 1),
                             Point(pos.y, pos.x - 1), Point(pos.y, pos.x + 1),
                             Point(pos.y + 1, pos.x - 1), Point(pos.y + 1, pos.x), Point(pos.y + 1, pos.x + 1)]:
            flash(increase_pos, board, flashed)

    pass


def board_step(board):
    flashed = set()
    print("")
    for y, row in enumerate(board):
        for x, _ in enumerate(row):
            board[y][x] += 1
            if board[y][x] > 9:
                flash(Point(y, x), board, flashed)
    for pos in flashed:
        # print(f"resetting position {pos}")
        board[pos.y][pos.x] = 0
    for row in board:
        print(f"{','.join([str(n) for n in row])}")

    print("")

    return len(flashed)


def run(data: str) -> Solution:
    board = [[(int(char)) for column in row for char in column] for row in data.splitlines()]
    print(f"boards: {board}")
    flash_count = 0
    for step in range(100):
        flash_count += board_step(board)

    return flash_count, step2(data)


def step2(data):
    board = [[(int(char)) for column in row for char in column] for row in data.splitlines()]
    for i, step in enumerate(range(1000)):
        print(f"step: {i}")
        if board_step(board) == 100:
            #expecting after..
            return i +1
    return 0
