"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton
jälkeen saadun silmäluvun.
"""
import random

def dice_roll():
    while True:
        print("Heitetään noppaa...")
        number = random.randint(1, 6)
        print(f"Tulokseksi saatiin {number}.")
        if number == 6:
            break

dice_roll()