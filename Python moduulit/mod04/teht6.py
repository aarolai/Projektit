import random

repeats = int(input("Syötä pisteiden pisteiden määrä: "))
amount = repeats


circle = 0

while repeats > 0:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        circle += 1

    repeats -= 1

pii = 4 * circle / amount


print(f"Piin likiarvo on: {pii}")