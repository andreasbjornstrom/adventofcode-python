'''
Test for year 2020, day 1 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2020.d01 import run

sample = '''1721
979
366
299
675
1456'''


def test_run() -> None:
  # not yet implemented!
  assert run(sample) == (514579, 241861950)
