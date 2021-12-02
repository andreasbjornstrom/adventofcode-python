'''
Solution for day 2 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 2` from the project root.
'''

from adventofcode.types import Solution


def part1(data: str):
    horizontal_position = 0
    depth = 0
    for row in data.splitlines():
        direction, count_str = row.split()
        count = int(count_str)
        print(f"going {direction} {count} steps")
        if direction == 'forward':
            horizontal_position += count
        if direction == 'up':
            depth -= count
        if direction == 'down':
            depth += count
        if depth < 0:
            depth = 0
    return horizontal_position * depth


def part2(data: str):
    horizontal_position = 0
    depth = 0
    aim = 0
    for row in data.splitlines():
        direction, count_str = row.split()
        count = int(count_str)
        print(f"going {direction} {count} steps")
        if direction == 'forward':
            horizontal_position += count
            depth += aim * count
        if direction == 'up':
            aim -= count
        if direction == 'down':
            aim += count
        if depth < 0:
            depth = 0

        print(horizontal_position, depth, aim)
    return horizontal_position * depth


def run(data: str) -> Solution:
    return part1(data), part2(data)


if __name__ == '__main__':
    run("")
