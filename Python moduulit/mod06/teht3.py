user_input = float(input("Syötä nestegallonimäärä: "))

def into_litres(gallons):
    litres = gallons * 3.785
    return litres

while user_input > 0:
    print(f"{user_input} gallonia on {into_litres(user_input)} litraa")
    user_input = float(input("Syötä nestegallonimäärä: "))
