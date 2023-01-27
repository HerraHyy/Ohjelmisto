"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan
vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä
syöttää negatiivisen gallonamäärän.

    Yksi gallona on 3,785 litraa.

"""
def fuel_convert():
    litres = gallon * 3.785
    return litres
gallon = int(input("Anna polttoiainemäärä US gallonoina: "))
while gallon > 0:
    litrat = fuel_convert()
    print(f"Polttoainemäärä litroina on {litrat}")
    gallon = int(input("Anna polttoiainemäärä US gallonoina: "))
    if gallon < 0:
        break