import functools

""" 
Opponent        Result
A   Rock        X   Lose
B   Paper       Y   Draw
C   Scissors    Z   Win
"""

hand_scores = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

outcome_scores = {
    "Lose": 0,
    "Draw": 3,
    "Win": 6,
}

response = {
    "Lose": {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"},
    "Draw": {"Rock": "Rock", "Paper": "Paper", "Scissors": "Scissors"},
    "Win": {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"},
}

translate = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Lose", "Y": "Draw", "Z": "Win"}

with open("./input-2.txt") as file:
    lines = file.readlines()


def score_line(line):
    opp = translate[line[0]]
    outcome = translate[line[2]]
    me = response[outcome][opp]
    return outcome_scores[outcome] + hand_scores[me]


total = functools.reduce(lambda total, line: total + score_line(line), lines, 0)
print(total)
