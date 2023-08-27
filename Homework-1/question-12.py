# Question-12: WAP to check whether the triangle is equilateral, isosceles, scalene or invalid sides are input by the user

# INPUT AREA
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))
# LOGIC AREA
if a == b == c:
    print("The triangle is equilateral")  # DISPLAYING AREA
elif a == b or b == c or a == c:
    print("The triangle is isosceles")  # DISPLAYING AREA
elif a != b or b != c or a != c:
    print("The triangle is scalene")  # DISPLAYING AREA
