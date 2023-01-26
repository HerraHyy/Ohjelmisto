import random
def die_roll():
    return random.randint(1, 6)
res = 0
while die_roll() != 6:
    res = die_roll()
    print(res)