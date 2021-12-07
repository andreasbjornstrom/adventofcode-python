'''
Test for year 2021, day 7 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2021.d07 import run, triangular_number


def test_run() -> None:
    assert triangular_number(1) == 1
    assert triangular_number(2) == 3
    assert triangular_number(3) == 6
    assert run('16,1,2,0,4,2,7,1,2,14') == (37, 168)
