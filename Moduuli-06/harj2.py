def inventaario(tavarat):
    tavarat.append("tussi")
    print("Sinulla on seuraavat tavarat:")
    for t in tavarat:
        print ("- " + t)
    return

koulureppu = ["kynä", "kumi", "viivoitin"]
inventaario(koulureppu)
print(koulureppu)