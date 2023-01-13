"""
Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
"""
import math
luku1 = input("Anna kokonaisluku 1: ")
luku2 = input("Anna kokonaisluku 2: ")
luku3 = input("Anna kokonaisluku 3: ")
sum = int(luku1) + int(luku2) + int(luku3)
multiply = int(luku1) * int(luku2) * int(luku3)
mean = int(sum) / 3
print(f"Lukujen summa on: {sum}, lukujen tulo on: {multiply} ja lukujen keskiarvo on: {mean} ")