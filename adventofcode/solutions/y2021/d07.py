'''
Solution for day 7 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 7` from the project root.
'''
from adventofcode.types import Solution


def part1(data):
    positions = [int(pos) for pos in data.split(",")]

    print(
        f"positions: {positions}, min: {min(positions)}, {max(positions)},"
        f" first try: {(max(positions) - min(positions)) / 2}")

    fuel_cost = None
    for goal in range(min(positions), max(positions)):
        _fuel_cost = sum([abs((pos - goal)) for pos in positions])
        print(f"trying out {goal}, resulted in {_fuel_cost}")
        if fuel_cost is None or _fuel_cost < fuel_cost:
            fuel_cost = _fuel_cost
        else:
            return fuel_cost


def triangular_number(n):
    return (n * (n + 1)) // 2


def part2(data):
    positions = [int(pos) for pos in data.split(",")]

    print(f"positions: {positions}, min: {min(positions)}, {max(positions)}")

    fuel_cost = None
    for target in range(min(positions), max(positions)):
        _fuel_cost = sum([triangular_number(abs((pos - target))) for pos in positions])
        print(f"trying out {target}, resulted in {_fuel_cost}")
        if fuel_cost is None or _fuel_cost < fuel_cost:
            fuel_cost = _fuel_cost
        else:
            return fuel_cost


def run(data: str) -> Solution:
    return part1(data), part2(data)
