import random

user_input = int(input("Syötä nopan tahkojen määrä: "))

def die_roll(maxroll):
    die = random.randint(1, maxroll)
    print(die)
    return die

roll = die_roll(user_input)

while roll != user_input:
    roll = die_roll(user_input)