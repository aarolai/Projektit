leiviska = input("Syötä leivisköjen määrä: ")
naula = input("Syötä naulojen määrä: ")
luoti = input("Syötä luotien määrä: ")

leiviska_paino = float(leiviska) * 20 * 32 * 13.3
naula_paino = float(naula) * 32 * 13.3
luoti_paino = float(luoti) * 13.3

kokonaispaino = (leiviska_paino + naula_paino + luoti_paino)

print(kokonaispaino)

kilogrammat = float(kokonaispaino/1000)

print(f"Kokonaispaino: {int(kilogrammat)} Kilogrammaa ja {(kilogrammat - int(kilogrammat)) *1000} grammaa")
