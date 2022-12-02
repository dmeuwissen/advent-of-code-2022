from enum import Enum


class OtherHand(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'


class YourHand(Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'


class RoundEnding(Enum):
    LOSE = 'X'
    WIN = 'Z'
    DRAW = 'Y'


WINS = [
    (YourHand.ROCK, OtherHand.SCISSORS),
    (YourHand.PAPER, OtherHand.ROCK),
    (YourHand.SCISSORS, OtherHand.PAPER)
]

DRAWS = [
    (YourHand.ROCK, OtherHand.ROCK),
    (YourHand.PAPER, OtherHand.PAPER),
    (YourHand.SCISSORS, OtherHand.SCISSORS)
]

LOSSES = [
    (YourHand.ROCK, OtherHand.PAPER),
    (YourHand.PAPER, OtherHand.SCISSORS),
    (YourHand.SCISSORS, OtherHand.ROCK)
]

HAND_SCORES = {YourHand.ROCK: 1, YourHand.PAPER: 2, YourHand.SCISSORS: 3}


def get_input():
    return [line.strip() for line in open("input.txt").readlines()]


def get_score_outcome(your_hand, other_hand):
    if (your_hand, other_hand) in WINS:
        return 6
    elif (your_hand, other_hand) in DRAWS:
        return 3
    elif (your_hand, other_hand) in LOSSES:
        return 0
    else:
        raise ValueError("Invalid input")


def get_score_hand(your_hand):
    return HAND_SCORES[your_hand]


def get_score(your_hand, other_hand):
    return get_score_hand(your_hand) + get_score_outcome(your_hand, other_hand)


def get_winning_hand(other_hand):
    for hands in WINS:
        if hands[1] == other_hand:
            return hands[0]


def get_losing_hand(other_hand):
    for hands in LOSSES:
        if hands[1] == other_hand:
            return hands[0]


def get_draw_hand(other_hand):
    for hands in DRAWS:
        if hands[1] == other_hand:
            return hands[0]


def get_my_hand_for_outcome(outcome, other_hand):
    if outcome == RoundEnding.WIN:
        return get_winning_hand(other_hand)
    elif outcome == RoundEnding.LOSE:
        return get_losing_hand(other_hand)
    elif outcome == RoundEnding.DRAW:
        return get_draw_hand(other_hand)
    else:
        raise ValueError("Invalid input")


def part_1(input_text):
    return sum([get_score(YourHand(hand), OtherHand(other_hand)) for other_hand, hand in
                [line.strip().split() for line in input_text]])


def part_2(input_text):
    total_score = 0
    for row in input_text:
        other_hand, round_ending = row.split()
        other_hand = OtherHand(other_hand)
        round_ending = RoundEnding(round_ending)

        my_hand = get_my_hand_for_outcome(round_ending, other_hand)
        total_score += get_score(my_hand, other_hand)

    return total_score


if __name__ == "__main__":
    input_text = get_input()
    print("Part 1:", part_1(input_text))
    print("Part 2:", part_2(input_text))
