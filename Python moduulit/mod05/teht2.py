num = input("Syötä luku: ")

numbers = []

while num != '':
    num = float(num)
    numbers.append(num)
    num = input("Syötä luku: ")

numbers.sort(reverse=True)


print(numbers[:5])