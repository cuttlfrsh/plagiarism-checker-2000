from random import randint

def guess_number():
    digit = randint(0, 100)
    guess = int(input("Guess the number between 0-100: "))
    while digit != guess:
        if guess > digit:
            print("Too high. Try again.")
        elif guess < digit:
            print("Too low. Try again.")
        guess = int(input("Guess the number between 0-100: "))
    print("Correct. Congratulations!")

guess_number()
