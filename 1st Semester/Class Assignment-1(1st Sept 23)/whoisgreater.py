# Question-5: Find the greatest of two numbers in python

# INPUT SECTION
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# LOGIC SECTION
c = a > b

# DISPLAY SECTION
print("First number is greater than the second"*c +
      "Second number is greater than the the first"*(1-c))
