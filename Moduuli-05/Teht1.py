"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja
tulostaa silmälukujen summan. Käytä for-toistorakennetta.
"""
import random
n = int(input("Anna arpakuutioiden lukumäärä: "))
sum = 0
for i in range(n):
    sum += random.randint(1, 6)
print(f"Arpakuutioiden silmälukujen summa on {sum}")
