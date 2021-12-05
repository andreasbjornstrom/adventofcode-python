'''
Solution for day 4 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 4` from the project root.
'''
from functools import reduce

from adventofcode.types import Solution


def get_match(board, sliding_winning_number):
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


def solution(data, break_on_first_win=False):
    rows = data.splitlines()
    drawn_numbers = [int(item) for item in rows.pop(0).split(",")]
    boards = create_boards(rows)

    sliding_winning_number = []
    boards_with_win = set()
    unmarked, current_number = 0, 0
    for drawn_number in drawn_numbers:
        current_number = drawn_number
        sliding_winning_number.append(current_number)
        unmarked, winning_board = calculate_winners(boards, break_on_first_win,
                                                    sliding_winning_number, boards_with_win)
        if winning_board is not None:
            print(f"..")
            break
    print(f"{unmarked} {current_number}")
    result = current_number, unmarked
    current_number, sum_of_unmarked = result
    return sum_of_unmarked * current_number


def calculate_winners(boards, break_on_first_win, sliding_winning_number, boards_with_win):
    for i, board in enumerate(boards):
        winning_row = get_match(board, sliding_winning_number)
        if winning_row is not None:
            flatten_board = [row for sublist in board for row in sublist]
            only_unmarked = set(flatten_board) - set(sliding_winning_number)
            sum_of_unmarked = reduce(lambda a, b: a + b, only_unmarked)
            boards_with_win.add(i)
            if break_on_first_win or len(boards) == len(boards_with_win):
                print(f"And we are done")
                return sum_of_unmarked, board
    return 0, None


def create_boards(rows):
    boards = []
    board = []
    row_counter = 1

    for i, row in enumerate(rows):
        if not row:
            continue
        board.append([int(number) for number in row.split()])
        if row_counter == 5:
            boards.append(board[:])
            row_counter = 0
            print(f"len of boards: {len(boards)}")
            board.clear()
        row_counter += 1
    return boards


def run(data: str) -> Solution:
    # not yet implemented!
    return solution(data, break_on_first_win=True), solution(data)
