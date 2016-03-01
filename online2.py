'''
Created on Feb 24, 2016

@author: Miranda Motsinger

Evaluates and prints the current score of a bowling game as it recieves
rolls one-by-one. The current score is the combined score of each
complete (fully-totalled) frame at that point in the game. Manages a list
of rolls representing the current frame that needs to be evaluated.
'''

import sys

rolls = []
curr_score = 0


# Evaluates frame score and deletes completed rolls off of rolls.
def frame_score(rolls):

    score = 0

    if len(rolls) == 3 and rolls[0] == 10:  # strike
        score += sum(rolls)
        rolls.pop(0)
    elif len(rolls) == 3 and rolls[0] + rolls[1] == 10:  # spare
        score += sum(rolls)
        rolls.pop(1)
        rolls.pop(0)

    if len(rolls) == 2 and rolls[0] + rolls[
            1] < 10:  # non-strike/spare complete frame
        score += sum(rolls)
        rolls.pop(1)
        rolls.pop(0)

    return score


for roll in sys.stdin:
    rolls.append(int(roll))
    curr_score = curr_score + frame_score(rolls)
    print(str(curr_score))