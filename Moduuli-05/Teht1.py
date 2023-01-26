"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja
tulostaa silmälukujen summan. Käytä for-toistorakennetta.
"""
import random
dice = input(int("Anna arpakuutioiden lukumäärä: "))
for i in range(dice):
    