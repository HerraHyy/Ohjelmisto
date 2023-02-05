"""
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen
etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla
"""
from geopy import distance

import mysql.connector

connection = mysql.connector.connect(
         host ='localhost',
         port = 3306,
         database = 'flight_game',
         user = 'Tomek2',
         password = '12345',
         autocommit = True
         )


# ap2 = input("Anna toisen lentokentän ICAO: ")
total = []
name = []
def airport_query1():
    print("Lasketaan kahden lentokentän välimatka kilometreinä.")
    for i in range(2):
        ap = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
        coord = ("Select name, latitude_deg, longitude_deg from airport where ident = '" + (ap) + "';")
        # print(coord)
        cursor = connection.cursor()
        cursor.execute(coord)
        result = cursor.fetchall()
        # print(result)
        total.append(result[0][1:])
        # print(total)
        name.append(result[0][0])
        print(*name)
    return
airport_query1()
print(f'Lentokenttien {name[0]} ja {name[1]} välimatka kilometreissä on: ')
print(distance.distance(total[0], total[1]).km)



