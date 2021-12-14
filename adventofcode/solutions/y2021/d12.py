'''
Solution for day 12 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 12` from the project root.
'''
import re
from collections import Counter

from adventofcode.types import Solution


def find_paths(rules):
    paths = set()
    ## has to start with start:
    for rule in rules:
        if rule.startswith("start-"):
            _, cave = rule.split("-")
            paths.add(f"start,{cave}")

    paths_len = -1
    while paths_len != len(paths):
        paths_len = len(paths)
        for rule in rules:
            if rule.startswith("start-") or rule.startswith("end-"):
                continue

            cave1, cave2 = rule.split("-")
            paths.update(generate_new_paths(cave1, cave2, paths))

    successful_paths = set()
    for path in paths:
        for rule in rules:
            last = path.split(",")[-1]

            if rule == f"end-{last}":
                successful_paths.add(f"{path},end")
    print(successful_paths)
    return successful_paths


def generate_new_paths(cave1, cave2, paths):
    new_paths = set()
    for path in paths:
        if path.endswith("-end"):
            continue

        last_cave = path.split(",")[-1]
        if cave1 == last_cave:
            if not cave2.isupper():
                if f",{cave2}" in path:
                    continue
            new_paths.add(f"{path},{cave2}")

        if cave2 == last_cave:
            if not cave1.isupper():
                if f",{cave1}" in path:
                    continue
            new_paths.add(f"{path},{cave1}")
    return new_paths


def part2(rules):
    print("part 2 started:")
    paths = set()
    ## has to start with start:
    for rule in rules:
        if rule.startswith("start-"):
            _, cave = rule.split("-")
            paths.add(f"start,{cave}")

    paths_len = -1
    while paths_len != len(paths):
        paths_len = len(paths)
        for rule in rules:
            print("#", end="")
            if rule.startswith("start-") or rule.startswith("end-"):
                continue

            cave1, cave2 = rule.split("-")
            print("*", end="")
            paths.update(generate_new_paths_2(cave1, cave2, paths))
            print("/", end="")
            paths = remove_some(paths)
            print("\\", end="")

    successful_paths = set()
    paths = remove_some(paths)
    for path in paths:
        for rule in rules:
            last = path.split(",")[-1]

            if rule == f"end-{last}":
                successful_paths.add(f"{path},end")
    print(successful_paths)
    return successful_paths


def remove_some(paths):
    new_paths = set()
    for path in paths:
        count = Counter(re.findall(f',[a-z]+?', path))
        #print(f"path:{path} {re.findall(f',[a-z]+?', path)}")
        if len(count.most_common(2)) > 1 and count.most_common(2)[1][1] > 1:
            #print(f"found too many {count.most_common(2)}")
            continue
        new_paths.add(path)
    return new_paths


def generate_new_paths_2(cave1, cave2, paths):
    new_paths = set()
    for path in paths:
        if path.endswith("-end"):
            continue

        last_cave = path.split(",")[-1]
        if cave1 == last_cave:
            if not cave2.isupper():
                if path.count(f",{cave2}") > 1:
                    continue

            new_paths.add(f"{path},{cave2}")

        if cave2 == last_cave:
            if not cave1.isupper():
                if path.count(f",{cave1}") > 1:
                    continue
            new_paths.add(f"{path},{cave1}")
    return new_paths


def run(data: str) -> Solution:
    paths = find_paths(data.splitlines())
    return len(paths), len(part2(data.splitlines()))
