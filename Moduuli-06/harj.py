def say_hello(to_whom):
    print(f"hello {to_whom}")  # funktion toiminto
    return "Valmista tuli"  # palauttaa arvon

result = say_hello("Kalle")
print(result)

def calculateSum(n1, n2):
#    result = n1 + n2
    return n1 + n2
print(calculateSum(10, 28))



# mod4t4 using function
import random
correctInt = random.randint(1, 10)
print(correctInt)
def check_guess(guess):
    if guess < correctInt:
        return "liian pieni arvaus."
    elif guess > correctInt:
        return "Liian suuri arvaus."
    else:
        return "Oikein arvattu."
def guess_game():
    game_on = True
    while game_on:
        user_guess = int(input("Arvaa luku 1-10: "))
        result = (check_guess(user_guess))
        print(result)
        if check_guess(user_guess) == "Oikein arvattu.":
            print("Game over")
            game_on = False
# guess_game()