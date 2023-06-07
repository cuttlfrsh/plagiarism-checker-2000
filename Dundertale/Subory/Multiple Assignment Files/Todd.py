# generate random integer values
from random import randint
guess = int(input("guess the number between 0-100: "))
digit = randint(0, 100)
while digit != guess:
    if guess > digit:
        print("too high. try again.")
    if guess < digit:
        print("too low. try again.")
    guess = int(input("guess the number between 0-100: "))
if digit == guess:
    print("correct. congratulations!")