# Question-4: WAP that takes user input of age and tell whether or not they are eligible to vote.

# INPUT SECTION
a = int(input("Enter your age: "))

# LOGIC SECTION
b = a >= 18

# DISPLAY SECTION
print("Yes you are eligble to vote"*b +
      "No, you are not eligible to vote"*(1-b))
