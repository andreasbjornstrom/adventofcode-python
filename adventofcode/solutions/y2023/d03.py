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


def part2(board):
    current_number = ""
    start_matches_count = 0
    star_position = "star"
    stars = {}

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if not is_number(cell):
                if start_matches_count == 1 and current_number != "":
                    stars.setdefault(star_position, []).append(
                        int(current_number))
                    print(star_position, int(current_number), stars)
                current_number = ""
                start_matches_count = 0
                star_position = None
            else:
                current_number += cell
                for direction in dirs:
                    pos = get_cell_data(
                        y, x, direction[0], direction[1], board)
                    if is_star(pos) and star_position != f"{y + direction[0]},{x + direction[1]}":
                        print("At cell", cell, " pos: ",
                              f"{y + direction[0]},{x + direction[1]}")
                        start_matches_count += 1
                        star_position = f"{y + direction[0]},{x + direction[1]}"

    if start_matches_count == 1 and current_number != "":
        stars[star_position] = stars[star_position] * int(current_number)

    return sum(star[0] * star[1] for star in stars.values() if len(star) > 1)


def _part2(board: [[]]) -> int:
    current_number = ""
    start_matches_counter = 0
    star_pos = "star"
    stars = {}

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if not is_number(cell):
                if start_matches_counter == 1 and current_number != "":
                    if star_pos not in stars.keys():
                        stars[star_pos] = [int(current_number)]
                        print(star_pos, int(current_number), stars)
                    else:
                        stars[star_pos].append(int(current_number))
                        print(star_pos, int(current_number), stars)
                current_number = ""
                start_matches_counter = 0
                star_pos = None
            else:
                current_number += cell
                for direction in dirs:
                    pos = get_cell_data(y, x, direction[0], direction[1], board)
                    if is_star(pos) and star_pos != f"{y + direction[0]},{x + direction[1]}":
                        print("At cell: ", cell, " pos: ",
                              f"{y + direction[0]},{x + direction[1]}")
                        start_matches_counter += 1
                        star_pos = f"{y + direction[0]},{x + direction[1]}"

    if start_matches_counter == 1 and current_number != "":
        stars[star_pos] = stars[star_pos] * int(current_number)

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
