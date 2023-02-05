"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna
airport-taulun ident-sarakkeeseen.
"""

import mysql.connector

yhteys = mysql.connector.connect(
         host ='localhost',
         port = 3306,
         database = 'flight_game',
         user = 'Tomek2',
         password = '12345',
         autocommit = True
         )
airport = input("Anna lentoaseman ICAO-koodi: ")

def airport_query():
    sql = "Select name from airport where ident = '" + (airport) + "';"
    # print(sql)
    entity_C = yhteys.cursor()
    # print("Yhdistetty mysql.")
    entity_C.execute(sql)
    result = entity_C.fetchone()
    print(result[0])
    if yhteys:
        yhteys.close()
        # print("Yhteys katkaistu.")
    return
airport_query()
