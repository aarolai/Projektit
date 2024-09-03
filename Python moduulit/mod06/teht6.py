import math

pizza1_diameter = float(input("Syötä ensimmäisen pizzan halkaisija: "))
pizza1_price = float(input("Syötä ensimmäisen pizzan hinta: "))

pizza2_diameter = float(input("Syötä toisen pizzan halkaisija: "))
pizza2_price = float(input("Syötä toisen pizzan hinta: "))

def value(price, diameter):
    surface_area = math.pi /4 * diameter**2
    worth = surface_area / price
    return worth

if value(pizza1_price, pizza1_diameter) > value(pizza2_price, pizza2_diameter):
    print("Ensimmäisellä pizzalla on rahasi arvoinen")
elif value(pizza1_price, pizza1_diameter) < value(pizza2_price, pizza2_diameter):
    print("Toinen pizza on rahasi arvoinen")
else:
    print("Kummatkin pizzat ovat hyviä valintoja")