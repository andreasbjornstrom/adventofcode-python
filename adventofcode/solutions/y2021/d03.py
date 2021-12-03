'''
Solution for day 3 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 3` from the project root.
'''
from adventofcode.types import Solution


def part1(data):
    rows = data.splitlines()
    gamma_rate = ""
    epsilon_rate = ""
    for column in range(0, len(rows[0])):
        count = 0
        sum = 0
        for row in rows:
            count += 1
            sum += int(row[column])

        if (count / 2) < sum:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
        print(f"Found: {count} {sum}, rows: {len(rows[0])}")

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2(data):
    rows = data.splitlines()
    oxygen_rating = find_rating(rows, default_bit=1)
    co2_rating = find_rating(rows, default_bit=0)

    print(f"Ratings:: {oxygen_rating} {co2_rating}")

    return int(oxygen_rating, 2) * int(co2_rating, 2)


def find_rating(rows, default_bit=0):
    patter_matcher = ""

    for column in range(0, len(rows[0])):
        rows_left = []
        sum_of_column = 0
        for row in rows:
            if not row.startswith(patter_matcher):
                continue
            sum_of_column += int(row[column])
            rows_left.append(row)

        if len(rows_left) == 1:
            return rows_left[0]

        if (len(rows_left) / 2) <= sum_of_column:
            patter_matcher += str(default_bit)
        else:
            patter_matcher += str(int(not default_bit))
    return patter_matcher


def run(data: str) -> Solution:
    return part1(data), part2(data)
