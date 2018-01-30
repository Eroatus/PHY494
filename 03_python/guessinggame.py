# guessinggame.py

import random

correct = False

number = random.randint(1, 100) # Secret Number

while not correct:
    guess = int(input("Guess the number (between 1 and 100, inclusive): "))

    if(guess < 1 or guess > 100):
        print("Your guess is out of bounds! Derp.")
    elif(guess > number):
        print("Your guess is too large.")
    elif(guess < number):
        print("Your guess is too small.")
    else:
        correct = True
        print("Your guess is correct.")
