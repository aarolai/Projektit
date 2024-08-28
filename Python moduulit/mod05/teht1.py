import random

value = 0

amount = int(input("Anna noppien määrä: "))

for i in range(amount):
    die_roll = random.randint(1,6)
    value += die_roll

print(f"Nopan silmälukujen summa on: {value}")

