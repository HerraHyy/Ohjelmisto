"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat
luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""


# num = input("Anna luku: ")
def is_prime_num(num):
    is_prime = True
    for i in range(2, num):
        print(f"testataan lukua jakamalla se arvolla {i}")
        print(f"jakojäännös on {num % i}")
        if num % i == 0:
            print(f"{num} ei ole alkuluku.")
            is_prime = False
        #    return False
        return f"{num} ei ole alkuluku."
    # return True
    return f"{num} on alkuluku."
print(is_prime_num(15))