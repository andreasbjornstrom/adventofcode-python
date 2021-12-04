'''
Solution for day 4 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 4` from the project root.
'''
from functools import reduce

from adventofcode.types import Solution


def part1(data):
    sum_of_unmarked, current_number = 0, 0
    rows = data.splitlines()
    drawn_numbers = rows[0].split(",")
    boards = []

    board_zero = []
    row_counter = 0
    for i, row in enumerate(rows):
        if i == 0 or not row:
            continue

        board_zero.append(row.split())
        row_counter += 1
        if row_counter == 5:
            boards.append(board_zero)
            print(board_zero)
            row_counter = 0
            print(f"len of boards: {len(boards)}")
            board_zero = []

    sliding_winning_number = []
    for drawn_number in drawn_numbers:
        sliding_winning_number.append(drawn_number)
        #       print(f"{sliding_winning_number}")
        winning_row = []
        for board in boards:
            winning_row = getMatch(board, sliding_winning_number)
            if winning_row is not None:
                all_in_board = [row for sublist in board for row in sublist]
                all_in_board_as_int = [int(col) for col in all_in_board]
                drawn_as_int = [int(col) for col in sliding_winning_number]
                only_unmarked = set(all_in_board_as_int) - set(drawn_as_int)
                sum_of_unmarked = reduce(lambda a, b: a + b, only_unmarked)
                current_number = int(drawn_number)
                break
        if winning_row is not None:
            print(f"..")
            break

    return sum_of_unmarked * current_number


def getMatch(board, sliding_winning_number):
    for r in range(0, 5):
        if set(board[r]) <= set(sliding_winning_number):
            print(f"yey!: {board[r]}")
            return board[r]
    for c in range(0, 5):
        col_values = []
        for r in range(0, 5):
            col_values.append(board[r][c])
        if set(sliding_winning_number) >= set(col_values):
            print(f"Win!: {col_values}")
            return col_values
    return None


def part2(data):
    sum_of_unmarked, current_number = 0, 0
    rows = data.splitlines()
    drawn_numbers = rows[0].split(",")
    boards = []

    board_zero = []
    row_counter = 0
    for i, row in enumerate(rows):
        if i == 0 or not row:
            continue

        board_zero.append(row.split())
        row_counter += 1
        if row_counter == 5:
            boards.append(board_zero)
            print(board_zero)
            row_counter = 0
            print(f"len of boards: {len(boards)}")
            board_zero = []

    sliding_winning_number = []
    boards_with_win = set()
    for drawn_number in drawn_numbers:
        sliding_winning_number.append(drawn_number)
      #  print(f"{sliding_winning_number}")
        winning_row = None
        for i, board in enumerate(boards):
            winning_row = getMatch(board, sliding_winning_number)
            if winning_row is not None:
                all_in_board = [row for sublist in board for row in sublist]
                all_in_board_as_int = [int(col) for col in all_in_board]
                drawn_as_int = [int(col) for col in sliding_winning_number]
                only_unmarked = set(all_in_board_as_int) - set(drawn_as_int)
                sum_of_unmarked = reduce(lambda a, b: a + b, only_unmarked)
                current_number = int(drawn_number)
                boards_with_win.add(i)
                if len(boards_with_win) == len(boards):
                    print(f"finally.. {winning_row}")
                    break
                winning_row = None
        if winning_row is not None:
            print(f"..")
            break
    print(f"{sum_of_unmarked} {current_number}")
    return sum_of_unmarked * current_number


def run(data: str) -> Solution:
    # not yet implemented!
    return part1(data), part2(data)
