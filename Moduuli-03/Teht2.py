"""
Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen
alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
"""
HyttiL = input("Anna laivan hyttiluokka: ")
if HyttiL == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif HyttiL == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif HyttiL == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif HyttiL == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else :
    print("Virheellinen hyttiluokka.")