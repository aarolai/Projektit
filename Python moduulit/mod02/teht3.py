kanta = input("Syötä kanta: ")
korkeus = input("Syötä korkeus: ")

kanta = float(kanta)
korkeus = float(korkeus)

piiri = kanta * 2 + korkeus * 2
pinta_ala = kanta * korkeus

print("Piiri on: " + str(piiri))
print("Suorakulmion pinta-ala: " + str(pinta_ala))