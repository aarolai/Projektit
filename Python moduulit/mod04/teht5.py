repeats = 0

while repeats < 6:
    username = input("Syötä käyttäjätunnus: ")
    password = input("Syötä salasana: ")
    if username == "python" and password == "rules":
        print("Tervetuloa")
        break
    elif repeats == 4:
        print("Pääsy evätty")
        break
    repeats = repeats + 1

