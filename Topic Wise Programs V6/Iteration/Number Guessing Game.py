"""
QUESTION: Write a Python program to guess a number between 1 and 9. User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""
from random import *

score = 10
while True:
    num = int(input("Guess a number between 1-9: "))
    guess = randrange(1,10)
    if num == guess:
        print("Well Guessed!!!")
        print(score)
        break
    else:
        print("Wrong Guess")
        score -= 1
        