'''
Solution for day 5 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 5` from the project root.
'''
from operator import itemgetter

from adventofcode.types import Solution


def get_hits(coordinate):
    p1 = coordinate[0]
    p2 = coordinate[1]
    hits = []
    # limit on part 1
    if p1[0] != p2[0] and p1[1] != p2[1]:
        print(coordinate)
        return []
    xs = [p2[0], p1[0]]
    ys = [p2[1], p1[1]]
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            hits.append((x, y))
    return hits


def part1(data):
    rows = data.splitlines()
    cordinates = [to_coordinate(row) for row in rows]
    hits = [get_hits(coordinate) for coordinate in cordinates]
    flatten = [item for sublist in hits for item in sublist]

    seen = set()
    multiple = set()
    for x in flatten:
        if x not in seen:
            seen.add(x)
        else:
            multiple.add(x)
    print(f"count: {len(multiple)}")
    return len(multiple)


def get_hits_with_diagonal(coordinate, include_diagonal = True):
    coordinate.sort(key=itemgetter(0, 1))
    p1 = coordinate[0]
    p2 = coordinate[1]
    hits = []
    if include_diagonal and p1[0] != p2[0] and p1[1] != p2[1]:
        adding = True if p1[1] < p2[1] else False
        print(coordinate)
        for i, x in enumerate(range(p1[0], p2[0] + 1)):
            hits.append((x,  (p1[1] + i if adding else p1[1] - i) ))
        return hits

    for x in range(p1[0], p2[0] + 1):
        for y in range(p1[1], p2[1] + 1):
            hits.append((x, y))
    return hits


def part2(data):
    rows = data.splitlines()
    cordinates = [to_coordinate(row) for row in rows]
    hits = [get_hits_with_diagonal(coordinate) for coordinate in cordinates]
    flatten = [item for sublist in hits for item in sublist]

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
#    {(0, 9),
#     (1, 9),
#     (2, 9),
#     (2, 2),
#     (3, 4),
#     (4, 4),
#     (7, 4),
#     (7, 1)}
#    - (2, 4),
#    -  (3, 3),


def to_coordinate(row):
    start, end = row.split("->")
    p1 = start.split(",")
    p2 = end.split(",")
    return [(int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1]))]


def run(data: str) -> Solution:
    # not yet implemented!
    return part1(data), part2(data)
