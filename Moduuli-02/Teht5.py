"""
Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
 Yksi leiviskä on 20 naulaa.
 Yksi naula on 32 luotia.
 Yksi luoti on 13,3 grammaa.

"""
import math
luoti = input("Syötä luodit: ")
naula = input("Syötä naulat: ")
leiviska = input("Syötä leiviskät: ")

summa = (((13.3 * int(luoti)) + int(naula) * 13.3 * 32) + int(leiviska) * 13.3 * 640) / 1000
gramma = (float(summa) - int(summa)) * 1000
print(f"paino on: {int(summa)} kiloa ja {int(gramma)} grammaa.")


