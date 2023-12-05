'''
Solution for day 1 of the 2023 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2023 1` from the project root.
'''
from adventofcode.types import Solution


def run(data: str) -> Solution:
    _data = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    __data = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    return (part1(data), part2(data))


def part1(data: str) -> int:
    sum = 0
    for line in data.splitlines():
        firstDigit = None
        lastDigit = None
        for char in line:
            firstDigit = returnIfChar(char)
            if firstDigit is not None:
                break

        for char in line[::-1]:
            lastDigit = returnIfChar(char)
            if lastDigit is not None:
                break

        print(firstDigit, lastDigit)

        sum += int(firstDigit + lastDigit)
    return sum


def returnIfChar(char: str):
    if char.isdigit():
        return char
    return None


def part2(data: str) -> int:
    sum = 0
    for line in data.splitlines():
        print(line)
        firstDigit = None
        lastDigit = None
        for pos, char in enumerate(line):
            firstDigit = matchLogic(line[pos:pos+5])
            if firstDigit is not None:
                break
        for pos, char in enumerate(line[::-1]):
            lastDigit = matchLogicFromEnd(line[::-1][pos:pos+5][::-1])
            if lastDigit is not None:
                break
        print(firstDigit, lastDigit)

        sum += int(firstDigit + lastDigit)
    return sum
# not yet implemented!


def matchLogic(partOfLine: str):
    print("searching in:", partOfLine)
    stringDigit = matches(partOfLine)
    if (stringDigit is not None):
        return stringDigit
    char = partOfLine[0]
    if char.isdigit():
        return char
    return None


def matches(s: str) -> bool:
    if s.startswith('one'):
        return "1"
    if s.startswith('two'):
        return "2"
    if s.startswith('three'):
        return "3"
    if s.startswith('four'):
        return "4"
    if s.startswith('five'):
        return "5"
    if s.startswith('six'):
        return "6"
    if s.startswith('seven'):
        return "7"
    if s.startswith('eight'):
        return "8"
    if s.startswith('nine'):
        return "9"
    return None


def matchLogicFromEnd(partOfLine: str):
    print("searching in:", partOfLine)
    stringDigit = matchesFromEnd(partOfLine)
    if (stringDigit is not None):
        return stringDigit
    char = partOfLine[-1]
    if char.isdigit():
        return char
    return None


def matchesFromEnd(s: str) -> bool:
    if s.endswith('one'):
        return "1"
    if s.endswith('two'):
        return "2"
    if s.endswith('three'):
        return "3"
    if s.endswith('four'):
        return "4"
    if s.endswith('five'):
        return "5"
    if s.endswith('six'):
        return "6"
    if s.endswith('seven'):
        return "7"
    if s.endswith('eight'):
        return "8"
    if s.endswith('nine'):
        return "9"
    return None
