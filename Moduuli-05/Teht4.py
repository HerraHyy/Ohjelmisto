"""
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien
kysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain
samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta
niiden läpikäymiseen.
"""
list = []
count = 1
print("Anna viisi kaupunkia yksi kerrallaan.")
for i in range(5):
    if count >= 1:
        city = input(f"Anna kaupunki {count}: ")
        list.append(city)
        count += 1
for city in list:
    print(city)