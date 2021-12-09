'''
Solution for day 8 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 8` from the project root.
'''
from adventofcode.types import Solution

one = 2
four = 4
seven = 3
eight = 7
two_three_five = 5
zero_six_nine = 6


def get_zero_six_nine(digit_set, chars_in_one, chars_in_four, chars_in_seven):
    if chars_in_one:
        if not chars_in_one.issubset(digit_set):
            return "6"
    if chars_in_four:
        if chars_in_four.issubset(digit_set):
            return "9"
    if chars_in_seven:
        if not chars_in_seven.issubset(digit_set):
            return "6"
    return "0"


def get_two_three_five(digit_set, one1, four_chars, seven_chars):
    if one1 and one1.issubset(digit_set):
        return "3"
    if seven_chars and seven_chars.issubset(digit_set):
        return "3"
    if four_chars and one1:
        diff = four_chars - one1
        if diff.issubset(digit_set):
            return "5"
    return "2"


def part2(data):
    extra_data = [row.split("|")[0].split() for row in data.splitlines()]
    four_digits_encoded = [row.split("|")[1].split() for row in data.splitlines()]
    total = 0
    for i, output_values in enumerate(four_digits_encoded):

        all_data = output_values + extra_data[i]
        all_data.sort(key=lambda x: len(x), reverse=True)
        chars_in_one = set()
        chars_in_four = set()
        chars_in_seven = set()
        for digit in all_data:
            letters_for_digit = set(digit)
            print(f"working with {len(digit)} {digit}")

            length = len(digit)
            if length == one:
                chars_in_one = letters_for_digit
            elif length == seven:
                chars_in_seven = letters_for_digit
            elif length == four:
                chars_in_four = letters_for_digit

        row_sum = ""
        for digit in output_values:
            length = len(digit)
            digit_set = set(digit)
            if length == one:
                row_sum += "1"
                continue
            elif length == four:
                row_sum += "4"
                continue
            elif length == seven:
                row_sum += "7"
                continue
            elif length == eight:
                row_sum += "8"
                continue

            if length == two_three_five:
                row_sum += get_two_three_five(digit_set, chars_in_one, chars_in_four, chars_in_seven)
            elif length == zero_six_nine:
                row_sum += get_zero_six_nine(digit_set, chars_in_one, chars_in_four, chars_in_seven)
        total += int(row_sum)

    return total


def part1(data):
    valid_numbers = [one, four, seven, eight]
    four_digits_encoded = [row.split("|")[1].split() for row in data.splitlines()]
    flatten = [digit for row in four_digits_encoded for digit in row]
    count = 0
    for digit in flatten:
        if len(digit) in valid_numbers:
            count += 1
    return count


def run(data: str) -> Solution:
    return (part1(data)), part2(data)
