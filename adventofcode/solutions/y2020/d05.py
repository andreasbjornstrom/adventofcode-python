'''
Solution for day 5 of the 2020 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2020 5` from the project root.
'''
from adventofcode.types import Solution


def find_row_and_seat(boarding_pass):
    row = 127
    steps = 64

    seat_steps = 4
    seat = 7
    for i, char in enumerate(boarding_pass):
        if i > 6:
            seat, seat_steps = bit_shift(char, seat, seat_steps)
            #           print(f"seat: {seat}, {seat_steps}")
            continue

        row, steps = bit_shift(char, row, steps)

    #       print(f"row: {row}, {steps}")
    return row, seat


def bit_shift(char, row_seat, steps):
    if char == 'F' or char == 'L':
        row_seat -= steps
    steps = steps >> 1
    return row_seat, steps


def calc_seat_id(seat):
    row = seat[0]
    seat = seat[1]
    return (row * 8) + seat


def run(data: str) -> Solution:
    seats = [find_row_and_seat(row) for row in data.splitlines()]
    seats.sort()
    print(len(seats))

    my_seat = get_my_seat(seats)

    seat_id = [calc_seat_id(seat) for seat in seats]
    seat_id.sort(reverse=True)
    return seat_id[0], calc_seat_id(my_seat)


def get_my_seat(seats):
    for i, seat in enumerate(seats):
        if i == 0:
            continue
        if seats[i - 1][0] == seat[0] - 1 or \
                seats[i - 1][1] == seat[1] - 1:
            continue
        print(f"probably mine, at: {i}, seat: {seat}, bad calculation = {i // 8}")
        # won't support row changes.
        return seat[0], seat[1] - 1
