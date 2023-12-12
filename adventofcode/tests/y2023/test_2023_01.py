'''
Test for year 2023, day 1 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2023.d01 import run

data1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
data2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def test_run() -> None:
    assert run(data1) == (142, 142)
    assert run(data2) == (None, None)
