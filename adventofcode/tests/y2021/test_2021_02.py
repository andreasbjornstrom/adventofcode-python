'''
Test for year 2021, day 2 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2021.d02 import run

data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def test_run() -> None:
  # not yet implemented!
  assert run(data) == (150, 900)

