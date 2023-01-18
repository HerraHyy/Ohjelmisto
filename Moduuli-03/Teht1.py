"""
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen,
ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta
sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.
"""
kuha = float(input("Anna kuhan mitta (cm): "))
if kuha >= 37:
    print("Kuha on täysimittainen. Bon appetit.")
elif kuha <= 37:
    vajaa = 37 - kuha
    print(f"Kuha on {vajaa:.2f} cm alamittainen. Laske kuha takaisin veteen.")