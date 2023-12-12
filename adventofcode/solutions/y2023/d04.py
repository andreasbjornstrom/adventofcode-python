'''
Solution for day 4 of the 2023 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2023 4` from the project root.
'''
from adventofcode.types import Solution


def run(data: str) -> Solution:
    result = 0
    for row in data.splitlines():
        (card, numbers) = row.split(": ")
        (winning, given) = numbers.split(" | ")
        winning_numbers = [int(item) for item in winning.split()]
        given_numbers = [int(item) for item in given.split()]
        count_matches = 0
        count_score = 0
        for number in given_numbers:
            if number in winning_numbers:
                count_matches += 1
                if count_matches == 1:
                    count_score = 1
                else:
                    count_score = count_score * 2
                print(f"{number} is a match")
        if count_matches > 0:
            result += count_score
            print(f"Card {card} has {count_matches} matches, current score: {result}")

    return result, None
