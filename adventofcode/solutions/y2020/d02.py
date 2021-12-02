'''
Solution for day 2 of the 2020 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2020 2` from the project root.
'''
from adventofcode.types import Solution


def part1(data):
    valid_passwords = 0

    for string in data.splitlines():
        interval, char_with_separator, password = string.split()
        char = char_with_separator[0]
        min_count, max_count = interval.split("-")

        count = password.count(char)
        if count < int(min_count) or count > int(max_count):
            continue
        valid_passwords += 1

    return valid_passwords


def part2(data):
    valid_passwords = 0

    for string in data.splitlines():
        interval, char_with_separator, password = string.split()
        char = char_with_separator[0]
        min_count, max_count = interval.split("-")

        if (password[int(min_count) - 1] == char) != \
                (password[int(max_count) - 1] == char):
            valid_passwords += 1
        continue

    return valid_passwords


def run(data: str) -> Solution:
    return part1(data), part2(data)
