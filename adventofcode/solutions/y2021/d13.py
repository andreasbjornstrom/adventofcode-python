'''
Solution for day 13 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 13` from the project root.
'''
import numpy as np

from adventofcode.types import Solution


def part1(data, part1=False):
    rows = [row for row in data.splitlines() if row and 'fold' not in row]
    board = np.zeros(
        (max([int(row.split(",")[1]) for row in rows]) + 1,
         max([int(row.split(",")[0]) for row in rows]) + 1))
    for row in data.splitlines():
        if not row:
            continue
        if 'fold along x=' in row:
            # reverse needed
            x = int(row.split("=")[1])
            base = board[:, 0:x]
            fold = board[:, x + 1:]
            reversed = np.flip(fold[::-1])
            print(base, "\n", reversed, "\n")
            board = base + reversed
            print(board)
            if part1:
                return board
            continue
        if 'fold along y=' in row:
            print("folding..")
            y = int(row.split("=")[1])
            base = board[0:y, :]
            fold = board[y + 1:, :]
            reversed = np.fliplr(np.flip(fold))
            print(base, "\n", reversed, "\n", fold)
            board = base + reversed
            print(board)
            if part1:
                return board
            continue
        y, x = [int(c) for c in row.split(",")]
        board[x][y] = 1
    return board


def run(data: str) -> Solution:
    return np.count_nonzero(part1(data, part1=True)), part1(data, part1=False)
