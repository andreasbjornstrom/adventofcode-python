"""
Solution for day 3 of the 2023 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2023 3` from the project root.
"""
from adventofcode.types import Solution


def run(data: str) -> Solution:
    board = [[*row] for row in data.splitlines()]
    return part1(board), part2(board)


dirs = [(-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)]


def _part2(board: [[]]) -> int:
    current_number = ""
    star_matches_counter = 0
    coordinates_for_star = "star"
    stars = {}

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if not is_number(cell):
                if star_matches_counter == 1 and current_number != "":
                    if coordinates_for_star not in stars.keys():
                        stars[coordinates_for_star] = [int(current_number)]
                        print(coordinates_for_star, int(current_number), stars)
                    else:
                        stars[coordinates_for_star].append(int(current_number))
                        print(coordinates_for_star, int(current_number), stars)
                current_number = ""
                star_matches_counter = 0
                coordinates_for_star = None
            else:
                current_number += cell
                for direction in dirs:
                    pos = get_cell_data(y, x, direction[0], direction[1], board)
                    coordinates_for_pos = f"{y + direction[0]},{x + direction[1]}"
                    if is_star(pos) and coordinates_for_star != coordinates_for_pos:
                        print("At cell: ", cell, " pos: ",
                              coordinates_for_pos)
                        star_matches_counter += 1
                        coordinates_for_star = coordinates_for_pos

    if star_matches_counter == 1 and current_number != "":
        stars[coordinates_for_star] = stars[coordinates_for_star] * int(current_number)

    result = 0
    for star in stars.values():
        if len(star) > 1:
            result += star[0] * star[1]
    return result


def part1(board: [[]]) -> int:
    result = 0

    current_number = ""
    valid_number = False
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if not is_number(cell):
                if valid_number:
                    print(current_number)
                    result += int(current_number)
                current_number = ""
                valid_number = False
            else:
                current_number += cell

                for direction in dirs:
                    pos = get_cell_data(y, x, direction[0], direction[1], board)
                    if not is_dot(pos) and not is_number(pos):
                        valid_number = True
                        break
    if valid_number:
        result += int(current_number)

    return result


def get_cell_data(i, j, y, x, board):
    if i + y < 0 or i + y >= len(board):
        return '.'
    row = board[i + y]

    if j + x < 0 or j + x >= len(row):
        return '.'
    return row[j + x]


def is_star(cell: str) -> bool:
    return cell == '*'


def is_dot(cell: str) -> bool:
    return cell == '.'


def is_number(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False
