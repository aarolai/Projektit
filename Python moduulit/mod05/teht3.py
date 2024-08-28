num = int(input("Syötä kokonaisluku: "))

count = 0

for i in range(1, num):
    if num % i == 0:
        count = count + 1

if count > 2:
    print("Tämä ei ole alkuluku")
else:
    print("Tämä on alkuluku")
