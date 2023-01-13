# moduuli-02, tehtävä 2
# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan. pi*r^2
import math
r = float(input("Anna ympyrän säde (m): "))
area = math.pi * r**2
# area = math.pi * r * r
print(f"Ympyrän pinta-ala on: {area:.2f} neliömetriä.")
