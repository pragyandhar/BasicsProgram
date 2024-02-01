# Question-1: Write a program that converts number of days to weeks and days

# INPUT SECTION
a = int(input("Enter the number of days: "))

# LOGIC SECTION
b = a//7
c = (a % 7)

# DISPLAY SECTION
print(a, "days are", b, "weeks and", c, "days")
