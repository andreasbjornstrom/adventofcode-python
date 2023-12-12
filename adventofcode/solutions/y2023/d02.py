'''
Solution for day 2 of the 2023 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2023 2` from the project root.
'''
from adventofcode.types import Solution


def run(data: str) -> Solution:
    return (part1(data), part2(data))


def part2(data: str) -> Solution:
    for line in data.splitlines():
        result = 0
        (gameNumber, games) = line.split(':')
        red = 0
        green = 0
        blue = 0
        for game in games.split(';'):
            for amountWithColor in game.strip().split(','):
                amount, color = amountWithColor.strip().split(' ')
                if color == 'red' and int(amount) > red:
                    red = int(amount)
                if color == 'green' and int(amount) > green:
                    green = int(amount)
                if color == 'blue' and int(amount) > blue:
                    blue = int(amount)

        result += red * green * blue
    return result


def part1(data: str) -> Solution:

    red = 12
    green = 13
    blue = 14
    result = 0
    for line in data.splitlines():
        includeGame = True
        (gameNumber, games) = line.split(':')
        for game in games.split(';'):
            for amountWithColor in game.strip().split(','):
                amount, color = amountWithColor.strip().split(' ')
                if color == 'red' and int(amount) > red:
                    includeGame = False
                if color == 'green' and int(amount) > green:
                    includeGame = False
                if color == 'blue' and int(amount) > blue:
                    includeGame = False

        if includeGame:
            result += int(gameNumber.split(' ')[1])
    return result
