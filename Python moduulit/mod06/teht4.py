list = []

amount = int(input("Syötä kuinka monen numeron summan haluat laskea: "))

for i in range(amount):
    user_input = float(input("Syötä numero: "))
    list.append(user_input)


def list_sum(x):
    numbers_summed = sum(x)
    return numbers_summed

print(f"Numeroiden summa on: {list_sum(list)}")