'''
Solution for day 5 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 5` from the project root.
'''
from operator import itemgetter

from adventofcode.types import Solution


def solution(data, include_diagonal):
    coordinates = [to_coordinate(row) for row in data.splitlines()]
    vent_positions = [get_hits_with_diagonal(coordinate, include_diagonal) for coordinate in coordinates]
    flatten = [item for sublist in vent_positions for item in sublist]

    seen = set()
    multiple = set()
    for x in flatten:
        if x not in seen:
            seen.add(x)
        else:
            multiple.add(x)
    flatten.sort(key=itemgetter(0, 1))
    print(f"hits: {len(flatten)}, count: {len(multiple)}")
    return len(multiple)


def get_hits_with_diagonal(coordinate, include_diagonal=True):
    coordinate.sort(key=itemgetter(0, 1))
    p1 = coordinate[0]
    p2 = coordinate[1]
    hits = []
    if p1[0] != p2[0] and p1[1] != p2[1]:
        if not include_diagonal:
            return hits
        adding = True if p1[1] < p2[1] else False
        for i, x in enumerate(range(p1[0], p2[0] + 1)):
            hits.append((x, (p1[1] + i if adding else p1[1] - i)))
        return hits

    xs = [p2[0], p1[0]]
    ys = [p2[1], p1[1]]
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            hits.append((x, y))
    return hits


def to_coordinate(row):
    start, end = row.split("->")
    p1 = start.split(",")
    p2 = end.split(",")
    return [(int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1]))]


def run(data: str) -> Solution:
    # not yet implemented!
    return solution(data, False), solution(data, True)
