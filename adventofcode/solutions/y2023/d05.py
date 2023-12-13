'''
Solution for day 5 of the 2023 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2023 5` from the project root.
'''
from adventofcode.types import Solution


def part1(data):
    # destination range start, the source range start, and the range length
    current_map = ""
    parsed_data = {}
    seeds = []
    row: str
    for row in data.splitlines():
        if row == "":
            continue
        if row.startswith("seeds:"):
            seeds = [int(item) for item in row.split()[1:]]
            continue
        if row == "seed-to-soil map:":
            current_map = "seed-to-soil map"
            continue
        if row == "soil-to-fertilizer map:":
            current_map = "soil-to-fertilizer map"
            continue
        if row == "fertilizer-to-water map:":
            current_map = "fertilizer-to-water map"
            continue
        if row == "water-to-light map:":
            current_map = "water-to-light map"
            continue
        if row == "light-to-temperature map:":
            current_map = "light-to-temperature map"
            continue
        if row == "temperature-to-humidity map:":
            current_map = "temperature-to-humidity map"
            continue
        if row == "humidity-to-location map:":
            current_map = "humidity-to-location map"
            continue
        (destination, source, length) = row.split()
        parsed_data.setdefault(current_map, [])
        parsed_data[current_map].append((int(destination), int(source), int(length)))

    goal = -1
    for seed in seeds:
        soilToSeed = parsed_data["seed-to-soil map"]
        soil = find_next(soilToSeed, seed)
        fertilizerToSoil = parsed_data["soil-to-fertilizer map"]
        fertilizer = find_next(fertilizerToSoil, soil)
        waterToFertilizer = parsed_data["fertilizer-to-water map"]
        water = find_next(waterToFertilizer, fertilizer)
        lightToWater = parsed_data["water-to-light map"]
        light = find_next(lightToWater, water)
        temperatureToLight = parsed_data["light-to-temperature map"]
        temperature = find_next(temperatureToLight, light)
        humidityToTemperature = parsed_data["temperature-to-humidity map"]
        humidity = find_next(humidityToTemperature, temperature)
        locationToHumidity = parsed_data["humidity-to-location map"]
        location = find_next(locationToHumidity, humidity)
        print(f"Seed {seed} is at location {location}")
        if location < goal or goal == -1:
            goal = location

    return goal


def find_next(listOfThings, seed) -> int:
    for (destination, source, length) in listOfThings:
        if seed >= source and seed < source + length:
            return destination + seed - source
    return seed


def part2(data):
    pass


def run(data: str) -> Solution:
    return part1(data), part2(data)
