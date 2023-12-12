'''
Test for year 2023, day 3 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2023.d03 import run


def test_run() -> None:
    data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    # not yet implemented!
    assert run(data) == (4361, 467835)
