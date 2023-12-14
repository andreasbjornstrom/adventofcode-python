'''
Solution for day 5 of the 2023 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2023 5` from the project root.
'''
from adventofcode.types import Solution


def walk(param: str, input_table, ranges):
    print("walking: ", param, input_table, ranges)
    next_range = []
    for seed in ranges:
        next_range.append(find_next_(input_table[param], seed))

    index = states.index(param)
    if index == len(states) - 1:
        return next_range
    return walk(states[index + 1], input_table, next_range)


def find_next_(list_of_things, seed) -> int:
    for (destination, source, length) in list_of_things:
        if source <= seed < source + length:
            return destination + seed - source
    return seed


states = ["seed-to-soil map:",
          "soil-to-fertilizer map:",
          "fertilizer-to-water map:",
          "water-to-light map:",
          "light-to-temperature map:",
          "temperature-to-humidity map:",
          "humidity-to-location map:"]


def part2(data):
    pass


def part1(data):
    # destination range start, the source range start, and the range length
    current_state = ""
    parsed_data = {}
    ranges = []

    row: str
    for row in data.splitlines():
        if row == "":
            continue
        if row.startswith("seeds:"):
            ranges = [int(item) for item in row.split()[1:]]
            continue

        if " map" in row:
            current_state = row
            continue
        (destination, source, length) = row.split()
        parsed_data.setdefault(current_state, [])
        parsed_data[current_state].append((int(destination), int(source), int(length)))

    goal = walk(states[0], parsed_data, ranges)
    return min(goal)


def run(data: str) -> Solution:
    return part1(data), part2(data)
