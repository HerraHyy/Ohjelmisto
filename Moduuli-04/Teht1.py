"""
Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
"""

# for numero in range (3, 1001, 3):
#    print (numero)

# luku = range (1, 1000)
# while int(luku%3 == 0):
#     print(luku)

alku = 1
loppu = 1000
div = 3
while (alku<=loppu):
    alku+=1
    if alku%div == 0:
        print(alku)
