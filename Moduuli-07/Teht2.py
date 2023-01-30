"""
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen
syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi
ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.
"""
names = set()
name = input("Anna nimi tai lopeta 'enter': ")
while name != "":
    if name in names:
        print("Aiemmin syötetty nimi.")
    else:
        names.add(name)
        print("Uusi nimi lisätty.")
    name = input("Anna seuraava nimi tai lopeta 'enter': ")
print(names)