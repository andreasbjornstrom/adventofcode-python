'''
Solution for day 3 of the 2020 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2020 3` from the project root.
'''
from adventofcode.types import Solution


def part1(data):
    count = 0
    position = 0

    for i, row in enumerate(data.splitlines()):
        if i == 0:
            position += 3
            continue
        while len(row) < position:
            row += row

        if row[position] == "#":
            count += 1

        position += 3
    return count


'''

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

'''


def part2(data):
    return slope_checker(data, 1, 1) * \
           slope_checker(data, 3, 1) * \
           slope_checker(data, 5, 1) * \
           slope_checker(data, 7, 1) * \
           slope_checker(data, 1, 2)


def slope_checker(data, right, down):
    count = 0
    position = 0
    for i, row in enumerate(data.splitlines()):
        if i < down:
            print(f"dissing line: {i}")
            position = right
            continue
        if (i % down) != 0:
            print(f"dissing line: {i}")
            continue

        while len(row) < position + 1:
            row += row

        print(f"Looking at i={i} position={position} {row[position]}")
        if row[position] == "#":
            count += 1

        position += right
    return count


def run(data: str) -> Solution:
    return part1(data), part2(data)
