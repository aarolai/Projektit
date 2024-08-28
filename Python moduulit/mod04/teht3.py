num = float(input("Syötä luku: "))

big = num
small = num

while True:
    answer = input("Syötä luku: ")
    if answer == "":
        break
    try:
        num = float(answer)
        big = max(big, num)
        small = min(small, num)
    except ValueError:
        print("Syötä kelvollinen luku")
print(f"Isoin luku: {big}")
print(f"Pienin luku: {small}")