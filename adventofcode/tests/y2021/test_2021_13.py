'''
Test for year 2021, day 13 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
import numpy as np

from adventofcode.solutions.y2021.d13 import run

data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def test_run() -> None:
    part1, part2 = run(data)
    assert np.array_equal(part2, np.array([[1., 1., 1., 1., 1.],
                                           [1., 0., 0., 0., 1.],
                                           [1., 0., 0., 0., 1.],
                                           [1., 0., 0., 0., 1.],
                                           [1., 2., 2., 1., 1.],
                                           [0., 0., 0., 0., 0.],
                                           [0., 0., 0., 0., 0.]]))
    assert part1 == 17
