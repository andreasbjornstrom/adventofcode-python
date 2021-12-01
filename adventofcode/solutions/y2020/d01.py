'''
Solution for day 1 of the 2020 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2020 1` from the project root.
'''
from adventofcode.types import Solution


def solution_1_short():
  for i, value in enumerate(data):
    for n, compare_to in enumerate(data):
      if value + compare_to == 2020:
        print(f"{value} {compare_to}")
        break


def run(data: str) -> Solution:
  print(data)
  return (None, None)
