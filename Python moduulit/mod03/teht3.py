blood = input("Syötä hemogobliiniarvosi g/l formaattina: ")
sex = input("Syötä biologinen sukupuolesi: ")

if sex == "Mies":
    if float(blood) < 134:
        print("Hemogobliiniarvosi on alhainen")
    elif float(blood) > 195:
        print("Hemogobliiniarvosi on korkea")
    elif 134 <= float(blood) <= 195:
        print("Hemogobliiniarvosi on normaali")
    else:
        print("Virheellinen syöte")
elif sex == "Nainen":
    if float(blood) < 117:
        print("Hemogobliiniarvosi on alhainen")
    elif float(blood) > 175:
        print("Hemogobliiniarvosi on korkea")
    elif 117 <= float(blood) <= 175:
        print("Hemogobliiniarvosi on normaali")
    else:
        print("Virheellinen syöte")

