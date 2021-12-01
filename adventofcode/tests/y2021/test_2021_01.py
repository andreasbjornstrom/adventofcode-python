'''
Test for year 2021, day 1 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2021.d01 import run

data = """199
200
208
210
200
207
240
269
260
263
"""

def test_run() -> None:
  # not yet implemented!
  assert run(data) == (7, 5)
