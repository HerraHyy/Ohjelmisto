"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""
import random
sides = int(input("Anna nopan tahkojen yhteismäärä: "))
def dice_roll(min, max):
    while True:
        print("Heitetään noppaa...")
        number = random.randint(1, sides)
        print(f"Tulokseksi saatiin {number}.")
        if number == sides:
            break

dice_roll(min, max)