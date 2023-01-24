"""
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
"""
tuumat = int(input("Anna tuumamäärä: "))
while tuumat >= 0:
    sentit = tuumat * 2.54
    print(sentit)
    tuumat = int(input("Anna tuumamäärä: "))
