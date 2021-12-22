'''
Test for year 2021, day 21 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2021.d21 import run


def test_run() -> None:
    data = """Player 1 starting position: 4
Player 2 starting position: 8"""

    assert run(data) == (739785, 444356092776315)
