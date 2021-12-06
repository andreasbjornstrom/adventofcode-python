'''
Solution for day 6 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 6` from the project root.
'''
import time

from adventofcode.types import Solution


class LanternFish:
    timer_til_fork: int

    def __init__(self, timer_til_fork):
        self.timer_til_fork = timer_til_fork

    def __repr__(self):
        return f"{self.timer_til_fork}"

    def evolve(self) -> bool:
        if self.timer_til_fork == 0:
            self.timer_til_fork = 6
            return True
        self.timer_til_fork -= 1
        return False


def part1(data):
    fishes = [LanternFish(int(age)) for age in data.split(",")]

    for day in range(0, 80):
        start = time.time()
        print(f"Generating: {day}")
        evolve = (lantern_fish.evolve() for lantern_fish in fishes)
        fishes += [LanternFish(8) for fork in evolve if fork]
        end = time.time()
        print(f"Took: {end - start}, generated {len(fishes)} fish")

    return len(fishes)


def part2(data):
    fish_age = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for age in data.split(","):
        fish_age[int(age)] += 1

    for day in range(0, 256):
        start = time.time()
        print(f"Generating: {day}")
        should_fork = fish_age.pop(0)
        fish_age.append(should_fork)
        fish_age[6] += should_fork
        end = time.time()
        print(f"{len(fish_age)}{fish_age}, {sum(fish_age)} fish, took {end - start}, ")

    return sum(fish_age)


# Each day, a 0 becomes a 6 and adds a new 8 to the end of the list,
# while each other number decreases by 1 if it was present at the start of the day.


def run(data: str) -> Solution:
    return part1(data), part2(data)
