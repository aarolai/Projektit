pituus = input("Syötä kuhan pituus: ")

erotus = 37 - float(pituus)

if float(erotus) >= 0:
    print(f"Kuhasi on {erotus} cm liian pieni")
