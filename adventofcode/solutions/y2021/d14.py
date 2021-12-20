'''
Solution for day 14 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 14` from the project root.
'''

from adventofcode.types import Solution


def count_chars(rules, template, steps):
    # Template:     NNCB NN NC CB
    # After step 1: NCNBCHB
    # After step 2: NBCCNBBBCBHCB
    # After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
    # After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
    pairs = {}
    first_char, last_char = template[0], template[-1]
    for i, char in enumerate(template):
        if i == 0:
            continue
        if template[i - 1] + char in pairs:
            pairs[template[i - 1] + char] += 1
        else:
            pairs[template[i - 1] + char] = 1


    print(rules)

    for _ in range(steps):
        new_pairs = {}
        for pair, current_count in pairs.items():
            p1, p2 = rules[pair]

            if p1 in new_pairs:
                new_pairs[p1] += current_count
            else:
                new_pairs[p1] = current_count

            if p2 in new_pairs:
                new_pairs[p2] += current_count
            else:
                new_pairs[p2] = current_count
        pairs = new_pairs
    #        print(pairs)

    chars = {}
    for pair in pairs:
        for c in pair:
            if c in chars:
                chars[c] += pairs[pair]
            else:
                chars[c] = pairs[pair]
    chars[first_char] += 1
    chars[last_char] += 1
    print(chars)
    return (max(chars.values()) - min(chars.values())) / 2


def run(data: str) -> Solution:
    rows = data.splitlines()
    rules2 = {}
    for row in rows[1:]:
        if "->" not in row:
            continue
        pair, new_char = row.split(" -> ", 2)
        rules2[pair] = (pair[0] + new_char, new_char + pair[1])
    part1 = count_chars(rules2, rows[0], 10)
    part2 = count_chars(rules2, rows[0], 40)
    return part1, part2
