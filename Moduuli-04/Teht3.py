"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
"""
pienin = suurin = 0
lukuStr = input("Anna luku. Tyhjä lopettaa: ")
if lukuStr != "":
    pienin = suurin = int(lukuStr)
while lukuStr != "":
    luku = int(lukuStr)
    if luku > suurin:
        suurin = luku
    lukuStr = input("Anna luku. Tyhjä lopettaa: ")
print(pienin)
print(suurin)