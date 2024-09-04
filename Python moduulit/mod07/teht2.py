names = {""}

user_input = input("Syötä nimi: ")
names.add(user_input)
print("Uusi nimi")

while user_input != "":
    user_input = input("Syötä nimi: ")
    if user_input in names:
        print("Aiemmin syötetty nimi")
    elif user_input not in names:
        print("Uusi nimi")
    names.add(user_input)

for x in names:
    print(x)