"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja
tulostaa silmälukujen summan. Käytä for-toistorakennetta.
"""
import random
n = int(input("Anna arpakuutioiden lukumäärä: "))
h = random.randint(1, 6)
for x in