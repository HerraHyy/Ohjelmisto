"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat
luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""
num = int(input("Anna kokonaisluku: "))
def is_prime(k):
    if k == 1:
       return print(f"{k} ei ole alkuluku.")
      #  return False
    if k == 2 or k == 3:
       return print(f"{k} on alkuluku.")
      #  return True
    if k % 2 == 0:
        return print(f"{k} ei ole alkuluku.")
      #  return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return print(f"{k} ei ole alkuluku.")
           # return False
    return print(f"{k} on alkuluku.")
    # return True
print(is_prime(num))






