"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää
uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman
syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy
ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
(ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
Löydät koodeja helposti selaimen avulla.)
"""
def add_airport():
    airport_name = input("Anna lentoaseman nimi: ")
    airport_icao = input("Anna lentoaseman ICAO-koodi: ")
    airports[airport_name] = airport_icao
    print("Lisätty!")
    return
                # Lisää peruuta tai palaa vaihtoehto

def search_airport():
    airport_search = input("Anna lentoaseman ICAO-koodi: ")
    if airport_search in airports:
        print(f"{airport_search} on {airports[airport_search]}")
    return

airports = {"Helsinki-Vantaan Lentoasema": "EFHK"}
choice = -1

while choice != 3:
    print("[1] Syötä uusi lentoasema.")
    print("[2] Hae lentoaseman tiedot.")
    print("[3] Lopeta")
    choice = int(input("Valinta: "))
    if choice == 1:
        add_airport()
    elif choice == 2:
        search_airport()
    elif choice == 3:
        print("Näkemiin!")
        break
    else:
        print("Virheellinen valinta.")
        print("[1] Syötä uusi lentoasema.")
        print("[2] Hae lentoaseman tiedot.")
        print("[3] Lopeta")
        choice = int(input("Valinta: "))