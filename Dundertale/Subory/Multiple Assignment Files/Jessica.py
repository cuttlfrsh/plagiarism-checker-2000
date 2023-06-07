import random

def guess_number():
    digit = random.randint(0, 100)
    while True:
        guess = int(input("Guess the number between 0-100: "))
        if guess > digit:
            print("Too high. Try again.")
        elif guess < digit:
            print("Too low. Try again.")
        else:
            print("Correct. Congratulations!")
            break

guess_number()
