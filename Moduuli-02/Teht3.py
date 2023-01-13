"""
Moduuli-02, tehtävä 3

Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
"""
import math
height = int(input("Anna suorakulmion kanta (m): "))
width = int(input ("Anna suorakulmion korkeus (m): "))
area = height * width
perimeter = width * 2 + height * 2
print(f"Suorakulmion piiri on {perimeter:.0f} metriä.")
print(f"Suorakulmion pinta-ala on {area:.0f} neliömetriä.")
