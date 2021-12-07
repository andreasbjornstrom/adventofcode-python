'''
Solution for day 4 of the 2020 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2020 4` from the project root.
'''
import re

from adventofcode.types import Solution


class Passport:
    byr: str = 0  # (Birth Year)
    iyr: str = 0  # (Issue Year)
    eyr: str = 0  # (Expiration Year)
    hgt: str = ""  # (Height)
    hcl: str = ""  # (Hair Color)
    ecl: str = ""  # (Eye Color)
    pid: str = ""  # (Passport ID)
    cid: str = ""  # (Country ID)

    def __init__(self, passport_as_string) -> None:
        for key_value in passport_as_string.split():
            key, value = key_value.split(":")
            # print(f"key: {key}, value: {value}")
            ## reqs python 3.10..
            if key == 'byr':
                self.byr = value
            elif key == 'iyr':
                self.iyr = value
            elif key == 'eyr':
                self.eyr = value
            elif key == 'hgt':
                self.hgt = value
            elif key == 'hcl':
                self.hcl = value
            elif key == 'ecl':
                self.ecl = value
            elif key == 'pid':
                self.pid = value
            elif key == 'cid':
                self.cid = value
            else:
                print("MEEEP?!")

    def __repr__(self) -> str:
        return f"\n has fields: byr: {self.byr},\n {self.iyr},\n {self.eyr},\n {self.hgt},\n {self.hcl},\n {self.pid},\n {self.cid}"

    def validate_part2(self) -> bool:
        valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return 1920 <= int(self.byr) <= 2002 and \
               2010 <= int(self.iyr) <= 2020 and \
               2020 <= int(self.eyr) <= 2030 and \
               self.validate_hgt() and \
               re.match('^#[0-9a-f]{6}$', self.hcl) and \
               self.ecl in valid_ecl and \
               re.match('^[0-9]{9}$', self.pid)

    def validate_part1(self) -> bool:
            return bool(self.byr) and \
                   bool(self.iyr) and \
                   bool(self.eyr) and \
                   bool(self.hgt) and \
                   bool(self.hcl) and \
                   bool(self.ecl) and \
                   bool(self.pid)

    def validate_hgt(self):
        if self.hgt.endswith("cm"):
            height, _ = self.hgt.split("cm")
            return 150 <= int(height) <= 193
        elif self.hgt.endswith("in"):
            height, _ = self.hgt.split("in")
            return 59 <= int(height) <= 76


def run(data: str) -> Solution:
    passports = [Passport(passport_lines) for passport_lines in data.split("\n\n")]
    print(passports)
    valid_passports1 = [passport for passport in passports if passport.validate_part1()]
    valid_passports2 = [passport for passport in passports if passport.validate_part2()]
    return len(valid_passports1), len(valid_passports2)
