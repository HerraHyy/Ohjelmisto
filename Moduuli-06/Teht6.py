"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota."""

import math
def pizza_estimator(halk, hinta):
    r1 = pizza1 // 2 / 100      # säde metreinä
    a1 = math.pi * r1 ** 2      # pinta-ala neliömetreinä
    r2 = pizza2 // 2 / 100
    a2 = math.pi * r2 ** 2
    value1 = hinta1 // a1       # Eurot per neliömetri, integer
    value2 = hinta2 // a2
    print(f"Ensimmäisen pizzan yksikköhinta per neliömetri on: {value1} euroa.")
    print(f"Toisen pizzan yksikköhinta per neliömetri on: {value2} euroa.")
    if value1 < value2:
        print("Ensimmäisen pizzan yksikköhinta on edullisempi.")
    else:
        print("Toisen pizzan yksikköhinta on edullisempi.")


pizza1 = int(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = int(input ("Anna ensimmäisen pizzan hinta euroina: "))
pizza2 = int(input("Anna toisen pizzan halkaisija: "))
hinta2 = int(input ("Anna toisen pizzan hinta euroina: "))
arvo1 = pizza_estimator(pizza1, hinta1)
# arvo2 = pizza_estimator(pizza2, hinta2)

