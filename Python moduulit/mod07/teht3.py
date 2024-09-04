choices = input("Uuden lentoaseman syöttäminen: 's' \n Lentoaseman hakeminen: 'h' \n Ohjelman lopetus: 'l'")

airports = {}

airports["EFHK"] = "Helsinki-Vantaa"


while choices != "l":
    if choices == "s":
        icao = input("Syötä lentokentän ICAO koodi: ")
        airport = input("Syötä lentokentän nimi koodi: ")
        airports[icao] = airport
    elif choices == "h":
        search = input("Syötä ICAO koodi: ")
        print(airports[search])
    else:
        print("Virheellinen syöttö")
    choices = input("Uuden lentoaseman syöttäminen: 's' \n Lentoaseman hakeminen: 'h' \n Ohjelman lopetus: 'l'")
