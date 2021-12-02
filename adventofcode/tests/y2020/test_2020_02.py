'''
Test for year 2020, day 2 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2020.d02 import run

data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


def test_run() -> None:
    # not yet implemented!

    assert run(data) == (2, 1)
