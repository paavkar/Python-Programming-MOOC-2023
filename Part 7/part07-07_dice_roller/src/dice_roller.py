# Write your solution here
from random import choice
def roll(die: str):
    a_dice = [3, 3, 3, 3, 3, 6]
    b_dice = [2, 2, 2, 5, 5, 5]
    c_dice = [1, 4, 4, 4, 4, 4]
    if(die == "A"):
        return choice(a_dice)
    elif(die == "B"):
        return choice(b_dice)
    elif(die == "C"):
        return choice(c_dice)
    
def play(die1: str, die2: str, times: int):
    d1_wins = 0
    d2_wins = 0
    ties = 0
    for i in range(times):
        first = roll(die1)
        second = roll(die2)
        if(first > second):
            d1_wins += 1
        elif(second > first):
            d2_wins += 1
        else:
            ties += 1
    return (d1_wins, d2_wins, ties)


### Example solution
from random import sample
def roll(die: str):
    dices = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }
 
    return sample(dices[die], 1)[0]
 
def play(die1: str, die2: str, times: int):
    v1 = 0
    v2 = 0
    t = 0
    for i in range(times):
        n1 = roll(die1)
        n2 = roll(die2)
        if n1>n2:
            v1 += 1
        elif n1<n2:
            v2 += 1
        else:
            t += 1
    return v1, v2, t
 