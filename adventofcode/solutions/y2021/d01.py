'''
Solution for day 1 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 1` from the project root.
'''
from adventofcode.types import Solution


def part1(data: str):
    increases = 0
    previous_value = None
    for i, depth in enumerate(data.splitlines()):
        if i == 0:
            previous_value = depth
            continue
        if int(depth) > int(previous_value):
            print(f"{int(depth)} (increases), pos: {i}")
            increases += 1
        else:
            print(f"{int(depth)} (decreases), pos: {i}")
        previous_value = depth
    return increases


def part2(data: str):
    previous = []
    counter = 0
    for i, depth in enumerate(data.splitlines()):
        depth_int = int(depth)

        if i > 2:
            current_depth = (sum(previous[1:]) + depth_int)
            if (sum(previous)) < current_depth:
                print(f"{current_depth} (increases), pos: {i}")
                counter += 1
            else:
                print(f"{int(current_depth)} (decreases), pos: {i}")
            previous.pop(0)
        previous.append(depth_int)

    return counter


def run(data: str) -> Solution:
    return part1(data), part2(data)
