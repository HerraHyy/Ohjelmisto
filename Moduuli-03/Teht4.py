"""
Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on
jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.
"""

# if jaollinen neljällä = karkausvuosi
# if jaollinen sadalla and neljälläsadalla = karkausvuosi
# else not

vl = int(input("kirjoita vuosiluku: "))
# jako = int (input("testaa onko vuosiluku jaollinen numerolla: "))
jako1 = 4
jako2 = 100
jako3 = 400

if (vl%jako3 != 0 and vl%jako2 == 0):
    print(f"Vuosi {vl} ei ole karkausvuosi.")
elif(vl%jako1 == 0):
    print(f"Vuosi {vl} on karkausvuosi.")
else:
    print(f"Vuosi {vl} ei ole karkausvuosi.")