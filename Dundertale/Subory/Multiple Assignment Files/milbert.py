from random import randint

def guess_number():
    digit = randint(0, 100)
    guess = int(input("Guess the number between 0-100: "))
    while True:
        if guess > digit:
            print("Too high. Try again.")
        elif guess < digit:
            print("Too low. Try again.")
        else:
            break
        guess = int(input("Guess the number between 0-100: "))
    print("Correct. Congratulations!")

guess_number()
