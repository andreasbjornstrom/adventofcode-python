'''
Solution for day 4 of the 2023 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2023 4` from the project root.
'''
from typing import Dict, Any

from adventofcode.types import Solution


def run(data: str) -> Solution:
    return part1(data), part2(data)


def part2(data: str) -> int:
    result: dict[int, int] = {}
    total_number_of_cards = len(data.splitlines())
    for row in data.splitlines():
        (card, numbers) = row.split(": ")
        print(card)
        (_, _card_number) = card.split()
        card_number = int(_card_number)
        result.setdefault(card_number, 0)
        result[card_number] += 1
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
        if count_matches > 0:
            print(result)
            for i in range(1, count_matches + 1):
                next_card = i + card_number
                if next_card > total_number_of_cards:
                    continue
                result.setdefault(next_card, 0)
                result[next_card] += result[card_number]
            print(f"Card {row} has {count_matches} matches, current score: {result}")

    return sum(result.values())


def part1(data: str) -> int:
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

    return result
