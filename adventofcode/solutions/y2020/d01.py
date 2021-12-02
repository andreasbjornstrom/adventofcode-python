'''
Solution for day 1 of the 2020 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2020 1` from the project root.
'''
from adventofcode.types import Solution


def solution_1(data):
    split_data = data.splitlines()
    for value in split_data:
        for compare_to in split_data:
            if int(value) + int(compare_to) == 2020:
                print(f"{value} {compare_to}")
                return int(value) * int(compare_to)


def solution_2(data):
    split_data = data.splitlines()
    for value_1 in split_data:
        for value_2 in split_data:
            for value_3 in split_data:
                if int(value_1) + int(value_2) + int(value_3) == 2020:
                    print(f"{value_1} {value_2} {value_3}")
                    return int(value_1) * int(value_2) * int(value_3)


def run(data: str) -> Solution:
    return solution_1(data), solution_2(data)
