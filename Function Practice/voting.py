# Write a function to tell user if he/she is able to vote or not.
def voting():
    if a >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")

a = int(input("Enter your age: "))
voting()