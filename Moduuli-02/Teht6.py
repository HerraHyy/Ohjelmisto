"""
teht 6
Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
    kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
    nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

Vihje: tutustu random.randint()-funktion käyttöön.
"""
import random

random_number1 = random.randint(0, 9)
random_number2 = random.randint(0, 9)
random_number3 = random.randint(0, 9)
lukko = f"{random_number1}{random_number2}{random_number3}"
print(f"3-numeroinen numerolukon koodi: {lukko}")

random_number4 = random.randrange(1, 7)
random_number5 = random.randrange(1, 7)
random_number6 = random.randrange(1, 7)
random_number7 = random.randrange(1, 7)
koodi = f"{random_number4}{random_number5}{random_number6}{random_number7}"
print(f"4-numeroinen lukon koodi: {koodi}")


