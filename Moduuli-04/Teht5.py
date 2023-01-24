"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin, tunnus
ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi
kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules).
"""
usern2 = "python"
passw2 = "rules"
tries = 1
usern1 = input("Anna käyttäjätunnus: ")
passw1 = input("Anna salasana: ")
while tries < 5 and usern1 != usern2 or passw1 != passw2:
    tries += 1
    print("Käyttäjätunnus tai salasana väärin.")
    usern1 = input("Anna käyttäjätunnus: ")
    passw1 = input("Anna salasana: ")
    if tries == 5:
        print("Pääsy evätty.")
        quit()
else:
    print("Tervetuloa.")
