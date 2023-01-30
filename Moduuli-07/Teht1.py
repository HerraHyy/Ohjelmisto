"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
(kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on
ensimmäinen talvikuukausi.
"""
vuodenajat = ("kevät", "kesä", "syksy", "talvi")
kuukausi = int(input("Anna kuukausi (1-12): "))
if kuukausi == 12 or kuukausi <= 2:
    vuodenaika = vuodenajat [3]
elif kuukausi <= 5:
    vuodenaika = vuodenajat [0]
elif kuukausi <= 8:
    vuodenaika = vuodenajat [1]
else:
    vuodenaika = vuodenajat [2]
print(vuodenaika)