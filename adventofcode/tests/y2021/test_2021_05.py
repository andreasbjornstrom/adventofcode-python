'''
Test for year 2021, day 5 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2021.d05 import run, get_hits_with_diagonal

data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def test_run() -> None:
    assert get_hits_with_diagonal([(0, 8), (8, 0)], True) == [(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7,1), (8,0)]
    assert get_hits_with_diagonal([(9, 7), (7, 9)], True) == [(7, 9), (8, 8), (9, 7)]
    assert get_hits_with_diagonal([(7, 9), (9, 7)], True) == [(7, 9), (8, 8), (9, 7)]
    assert get_hits_with_diagonal([(1, 1), (3, 3)], True) == [(1, 1), (2, 2), (3, 3)]
    assert run(data) == (5, 12)


if __name__ == '__main__':
    test_run()
