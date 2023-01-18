"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa,
onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
"""
sukupuoli = input("Anna sukupuolesi (M/N): ")
hemo = int(input("Anna hemoglobiiniarvosi: "))
if sukupuoli == "N":
    if hemo >= 117 and hemo <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    elif hemo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == "M":
    if hemo >= 134 and hemo <= 196:
        print("Hemoglobiiniarvosi on normaalin rajoissa.")
    elif hemo > 196:
        print("Hemoglobiiniarvosi on korkea.")
    elif hemo < 134:
        print("Hemoglobiiniarvosi on alhainen.")