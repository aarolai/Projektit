import random

def die_roll():
    die = random.randint(1, 6)
    print(die)
    return die

roll = die_roll()

while roll != 6:
    roll = die_roll()