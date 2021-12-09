'''
Solution for day 9 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 9` from the project root.
'''
from functools import reduce

from adventofcode.types import Solution


def do_stuff(row):
    return [char for char in row]


def find_low_points(board):
    lowest_points = []
    for y, row in enumerate(board):
        for x, char in enumerate(row):
            digit = int(char)
            if digit == 0:
                lowest_points.append((x, y))
                continue
            # print(f"x:{x}, y:{y} char:{char}")
            if y > 0 and int(board[y - 1][x]) <= digit:
                continue
            if len(board) > (y + 1) and int(board[y + 1][x]) <= digit:
                continue
            if x > 0 and int(board[y][x - 1]) <= digit:
                continue
            if len(board[y]) > (x + 1) and int(board[y][x + 1]) <= digit:
                continue

            lowest_points.append((x, y))

    return lowest_points


def find_basin(point, board, visited):
    if point in visited:
        print(f"Puh, already been here! {point}")
        return visited
    x = point[0]
    y = point[1]
    digit = int(board[y][x])
    print(f"at {point}, with digit; {digit}")
    visited.add(point)

    if y > 0 and \
            9 > int(board[y - 1][x]) > digit:
        find_basin((x, y - 1), board, visited)

    if x > 0 and \
            9 > int(board[y][x - 1]) > digit:
        find_basin((x - 1, y), board, visited)

    if len(board) > (y + 1) and \
            9 > int(board[y + 1][x]) > digit:
        find_basin((x, y + 1), board, visited)

    if len(board[y]) > (x + 1) and \
            9 > int(board[y][x + 1]) > digit:
        find_basin((x + 1, y), board, visited)

    return visited


def part2(board, points):
    print(f"lowest points: {points}")
    basins = [len(find_basin(point, board, set())) for point in points]
    basins.sort(reverse=True)
    return reduce((lambda x, y: x * y), basins[:3])


def run(data: str) -> Solution:
    rows = [row for row in data.splitlines()]
    board = [[char for char in row] for row in rows]
    points = find_low_points(board)
    part1 = sum([int(board[point[1]][point[0]]) for point in points]) + len(points)

    return part1, part2(board, points)
