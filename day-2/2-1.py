import functools

""" 
            Opponent    Me
Rock        A           X
Paper       B           Y
Scissors    C           Z
 """

hand_scores = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

outcome_scores = {
    "Loss": 0,
    "Draw": 3,
    "Win": 6,
}

outcomes = {
    "Rock": {"Rock": "Draw", "Paper": "Loss", "Scissors": "Win"},
    "Paper": {"Rock": "Win", "Paper": "Draw", "Scissors": "Loss"},
    "Scissors": {"Rock": "Loss", "Paper": "Win", "Scissors": "Draw"},
}

hands = {"A": "Rock", "X": "Rock", "B": "Paper", "Y": "Paper", "C": "Scissors", "Z": "Scissors"}

file = open("./input-2.txt")
lines = file.readlines()
file.close()


def score_line(line):
    opp = hands[line[0]]
    me = hands[line[2]]
    return outcome_scores[outcomes[me][opp]] + hand_scores[me]


total = functools.reduce(lambda total, line: total + score_line(line), lines, 0)

print(total)
