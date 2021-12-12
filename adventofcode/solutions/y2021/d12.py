'''
Solution for day 12 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 12` from the project root.
'''
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


def run(data: str) -> Solution:
    paths = find_paths(data.splitlines())
    return len(paths), None
