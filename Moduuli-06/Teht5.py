"""Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan, joka on
muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen
että karsitun listan."""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [i for i in list1 if i % 2 != 0]
def remove_evens(list1):
    for i in list1:
        if(i % 2 != 0):
            list1.remove(i)
print(list1)
remove_evens(list1)
print(list1)
# print(list2)