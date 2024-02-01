import random as r
comp = r.randrange(1,101)

while True:
    user = int(input("Guess the number from 1 to 100: "))
    if comp == user:
        print("You Win")
        break
    elif user < comp:
        print("Too Small")
    else:
        print("Too Large")
    