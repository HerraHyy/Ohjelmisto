"""
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien
lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65
kappaletta, helikopterikenttiä on 15 kappaletta jne.
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
country_code = input("Anna maakoodi (esim. FI): ")
def airport_query():
    sql = ("Select iso_country, count(*) as total, type "
           "from airport "
           "where iso_country = '" + (country_code) + "' "
           "group by type order by type desc;")
    print(sql)
    cursor = yhteys.cursor()
    # print("Yhdistetty mysql.")
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print(*x)
    if yhteys:
        yhteys.close()
        # print("Yhteys katkaistu.")
    return
airport_query()

