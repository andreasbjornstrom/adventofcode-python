'''
Test for year 2021, day 12 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2021.d12 import run

def test_run() -> None:
  # not yet implemented!
  assert run('''start-A
start-b
A-c
A-b
b-d
end-A
end-b''') == (10, None)
