# generate random integer values
from random import randint

number = randint(0, 100)

guess = int(input("guess the whole number between 0-100: "))

while number != guess:

    if guess > number:
        print("the number you chose is too high. try again.")
    if guess < number:
        print("the number you chose is too low. try again.")

    guess = int(input("guess the number between 0-100: "))

if number == guess:
    print("the number you chose is correct. congratulations!")

