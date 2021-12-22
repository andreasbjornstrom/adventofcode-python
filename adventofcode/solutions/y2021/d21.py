'''
Solution for day 21 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 21` from the project root.
'''

from adventofcode.types import Solution


class DeterministicDice:
    def __init__(self):
        self.current_roll = 0

    def next(self):
        if self.current_roll == 100:
            self.current_roll = 1
        else:
            self.current_roll += 1
        return self.current_roll


class Game:
    def __init__(self, p1, p2, max_score=1000):
        self.player_one_position = p1
        self.player_two_position = p2
        self.player_one_score = 0
        self.player_two_score = 0
        self.max_score = max_score

    def roll_player_one(self, dice_sum) -> bool:
        position = Game.get_new_position(self.player_one_position, dice_sum)
        self.player_one_position = position
        self.player_one_score += position
        print(f"player two: {self.player_one_position}, score: {self.player_one_score}")
        if self.player_one_score >= self.max_score:
            return True
        return False

    def roll_player_two(self, dice_sum):
        position = Game.get_new_position(self.player_two_position, dice_sum)
        self.player_two_position = position
        self.player_two_score += position
        print(f"player two: {self.player_two_position}, score: {self.player_two_score}")
        if self.player_two_score >= self.max_score:
            return True
        return False

    @staticmethod
    def get_new_position(current, roll):
        new_pos = current + roll
        print(f"{current} + {roll}")
        last_digit = int(str(new_pos)[-1])
        if last_digit == 0:
            return 10
        else:
            return last_digit


def part1(data):
    current_roll = 0
    dice = DeterministicDice()

    game = Game(int(data.splitlines()[0].split(": ")[1]), int(data.splitlines()[1].split(": ")[1]))
    while True:
        current_roll += 3
        dice_sum = dice.next() + dice.next() + dice.next()
        if game.roll_player_one(dice_sum):
            loosing_score = game.player_two_score
            print(f"{loosing_score} * {current_roll}")
            return current_roll * loosing_score
        current_roll += 3
        dice_sum = dice.next() + dice.next() + dice.next()
        if game.roll_player_two(dice_sum):
            loosing_score = game.player_one_score
            print(f"{loosing_score} * {current_roll}")
            return current_roll * loosing_score


def part2(data):
    pass


def run(data: str) -> Solution:
    # clockwise 1-10
    # random start, p1 goes first
    # roll three times
    # move forward
    # score same as placement
    # win at > 1000
    # determenistic, 1 -> 100 -> 1

    return part1(data), part2(data)
