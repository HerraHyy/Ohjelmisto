"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja
tulostaa silmälukujen summan. Käytä for-toistorakennetta.
"""
import random
n = int(input("Anna arpakuutioiden lukumäärä 1-10: "))
h = random.randint(1, 6)
for n in