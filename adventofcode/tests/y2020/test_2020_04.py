'''
Test for year 2020, day 4 solution.
Run tests from project root with `PYTHONPATH=$(pwd) py.test`.
'''
from adventofcode.solutions.y2020.d04 import run


def test_run() -> None:
    data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

iyr:2019
cid:314
eyr:2039 hcl:#cfa07d hgt:171cm ecl:#0180ce byr:2006 pid:8204115568

eyr:2026
hcl:#733820
pid:230583200 byr:1997
ecl:brn
iyr:2010
hgt:179cm"""

    assert run(data) == (4, 3)

if __name__ == '__main__':
    test_run()