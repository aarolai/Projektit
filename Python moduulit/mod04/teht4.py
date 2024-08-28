import random

num = random.randint(1, 10)

guess = int(input("Arvaa luku 1-10 väliltä: "))

while guess != num:
    if guess < num:
        print("Liian pieni arvaus")
    elif guess > num:
        print("Liian suuri arvaus")
    guess = int(input("Arvaa luku 1-10 väliltä: "))
print("Oikein")
