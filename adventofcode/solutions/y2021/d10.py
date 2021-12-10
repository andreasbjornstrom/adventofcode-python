'''
Solution for day 10 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 10` from the project root.
'''
from collections import Counter

from adventofcode.types import Solution

missing_parenthesis = 3
missing_bracket = 57
missing_bird = 1197
missing_duck_face = 25137


# point_scale=[('(', 3)]

def part1(data):
    allowed_dividers = ['(', '[', '{', '<']
    allowed_closing = [')', ']', '}', '>']
    illegal_chars = []

    for row in data.splitlines():

        expecting_closing = []
        for char in row:
            #            print(f"at char {char}")
            if char in allowed_dividers:
                expecting_closing += allowed_closing[allowed_dividers.index(char)]
            elif expecting_closing and char == expecting_closing[-1]:
                expecting_closing.pop()
                ## all good..
            else:
                print(f"found corrupted line, at char {char}! {row}")
                illegal_chars += char
                break
    return illegal_chars


def run(data: str) -> Solution:
    illegal_chars = part1(data)

    count = Counter(illegal_chars)

    part1_score = count[')'] * missing_parenthesis + \
                  count[']'] * missing_bracket + \
                  count['}'] * missing_bird + \
                  count['>'] * missing_duck_face
    return part1_score, None
