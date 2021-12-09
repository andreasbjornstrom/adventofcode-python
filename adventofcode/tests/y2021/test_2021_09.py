'''
Test for year 2021, day 9 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2021.d09 import run

def test_run() -> None:
  # not yet implemented!
  assert run(
      """2199943210
3987894921
9856789892
8767896789
9899965678""") == (15, 1134)


if __name__ == '__main__':
    test_run()