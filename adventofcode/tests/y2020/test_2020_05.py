'''
Test for year 2020, day 5 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2020.d05 import run

def test_run() -> None:
  # not yet implemented!
  data = '''FBFBBFFRL
FFFBBBFRRR'''
  assert run(data) == (357, 356)
