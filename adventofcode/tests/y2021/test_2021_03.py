'''
Test for year 2021, day 3 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2021.d03 import run

data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def test_run() -> None:
    # not yet implemented!
    assert run(data) == (198, 230)
