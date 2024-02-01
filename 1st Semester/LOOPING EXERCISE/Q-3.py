# Write a Python program to guess a number between 1 and 9.

# IMPORT SECTION
import random as r

# INSTRUCTION SECTION
print('''
1) You have to guess a number between 1-10
2) If your guess is correct then you will get +4 points
3) If your guess is wrong you will lose -1 point
      ''')

# INPUT SECTION
a = int(input("Guess a number between 1-10: "))

# LOGIC SECTION
b = r.randint(1,10)
c = 0
while a == b:
    print("CORRECT")
    c += 4
    print("Your points are:",c)
    break
while a != b:
    print("WRONG")
    c -= 1
    print("Your points are:",c)
    break
    


