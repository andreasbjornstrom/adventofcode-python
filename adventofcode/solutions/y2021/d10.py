'''
Solution for day 10 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 10` from the project root.
'''
from collections import Counter


# point_scale=[('(', 3)]
from adventofcode.types import Solution


def part1(data):
    allowed_dividers = ['(', '[', '{', '<']
    allowed_closing = [')', ']', '}', '>']
    illegal_chars = []
    expected_closings = []
    for row in data.splitlines():

        corrupt = False
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
                corrupt = True
                illegal_chars += char
                break
        if not corrupt:
            expected_closings.append(expecting_closing)
    return illegal_chars, expected_closings


def score(expecting_closings):
    missing_parenthesis = 1
    missing_bracket = 2
    missing_bird = 3
    missing_duck_face = 4
    scores = []
    for expected_closing in expecting_closings:
        score = 0
        expected_closing.reverse()
        print(f"working with {expected_closing}")
        for char in expected_closing:
            score *= 5
            if char == ')':
                score += missing_parenthesis
            if char == ']':
                score += missing_bracket
            if char == '}':
                score += missing_bird
            if char == '>':
                score += missing_duck_face
        scores.append(score)
        print(f"score: {score}")

    scores.sort()
    return scores[len(scores) // 2]


def run(data: str) -> Solution:
    illegal_chars, expecting_closing = part1(data)

    count = Counter(illegal_chars)
    missing_parenthesis = 3
    missing_bracket = 57
    missing_bird = 1197
    missing_duck_face = 25137
    part1_score = count[')'] * missing_parenthesis + \
                  count[']'] * missing_bracket + \
                  count['}'] * missing_bird + \
                  count['>'] * missing_duck_face
    return part1_score, score(expecting_closing)
