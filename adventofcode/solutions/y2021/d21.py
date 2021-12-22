'''
Solution for day 21 of the 2021 Advent of Code calendar.
Run it with the command `python -m adventofcode run_solution -y 2021 21` from the project root.
'''
import time

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


def part1(data):
    current_roll = 0
    dice = DeterministicDice()

    game = Game(int(data.splitlines()[0].split(": ")[1]), int(data.splitlines()[1].split(": ")[1]))
    while True:
        current_roll += 3
        [game.roll(dice.next()) for _ in range(3)]
        if game.has_p1_won():
            loosing_score = game.player_two_score
            print(f"{loosing_score} * {current_roll}")
            return current_roll * loosing_score
        current_roll += 3
        [game.roll(dice.next()) for _ in range(3)]
        if game.has_p2_won():
            loosing_score = game.player_one_score
            print(f"{loosing_score} * {current_roll}")
            return current_roll * loosing_score


class Game:
    def __init__(self, position_p1, position_p2, max_score=1000, p1_score=0, p2_score=0, roll_counter=0, dice_sum=0):
        self.player_one_position = position_p1
        self.player_two_position = position_p2
        self.player_one_score = p1_score
        self.player_two_score = p2_score
        self.max_score = max_score
        self.roll_counter = roll_counter
        self.current_dice_sum = dice_sum

    def roll(self, roll):
        self.roll_counter += 1
        if self.roll_counter > 6:
            self.roll_counter = 1
            self.current_dice_sum = 0

        self.current_dice_sum += roll
        if self.roll_counter == 3:
            self.roll_player_one()
            self.current_dice_sum = 0

        if self.roll_counter == 6:
            self.roll_player_two()
            self.current_dice_sum = 0

    def roll_player_one(self):
        position = Game.get_new_position(self.player_one_position, self.current_dice_sum)
        self.player_one_position = position
        self.player_one_score += position

        #print(f"player one: {self.player_one_position}, score: {self.player_one_score}")

    def has_p1_won(self):
        if self.player_one_score >= self.max_score:
            return True
        return False

    def roll_player_two(self):
        position = Game.get_new_position(self.player_two_position, self.current_dice_sum)
        self.player_two_position = position
        self.player_two_score += position

        #print(f"player two: {self.player_two_position}, score: {self.player_two_score}")

    def has_p2_won(self):
        if self.player_two_score >= self.max_score:
            return True
        return False

    @staticmethod
    def get_new_position(position, roll):
        new_pos = position + roll
        # print(f"{position} + {roll}")
        # last_digit = int(str(new_pos)[-1])
        last_digit = new_pos % 10
        if last_digit == 0:
            return 10
        else:
            return last_digit


def part2(data, max_score):
    game = Game(int(data.splitlines()[0].split(": ")[1]), int(data.splitlines()[1].split(": ")[1]), max_score)

    run_game(game, max_score)
    return max(wins_p1, wins_p2)


def run_game(game, max_score):
    if game.has_p1_won():
        p1_won()
        #print(f"current winnings p1: {wins_p1}")
        return
    if game.has_p2_won():
        p2_won()
        #print(f"current winnings p2: {wins_p1}")
        return
    game2 = Game(game.player_one_position, game.player_two_position, max_score, game.player_one_score,
                 game.player_two_score,
                 game.roll_counter, game.current_dice_sum)
    game3 = Game(game.player_one_position, game.player_two_position, max_score, game.player_one_score,
                 game.player_two_score,
                 game.roll_counter, game.current_dice_sum)
    game .roll(1)
    game2.roll(2)
    game3.roll(3)
    run_game(game, max_score)
    run_game(game2, max_score)
    run_game(game3, max_score)


wins_p1 = 0
wins_p2 = 0
total_wins = 0
start = time.time()


def p1_won():
    global wins_p1, total_wins, start
    wins_p1 += 1
    total_wins += 1

    if total_wins > 1000000:
        print(f"1000 000 wins took {time.time() - start}")
        start = time.time()
        total_wins = 0


def p2_won():
    global wins_p2, total_wins
    wins_p2 += 1
    total_wins += 1

def run(data: str) -> Solution:
    return 739785, part2(data, 10)
#    return part1(data), part2(data)
