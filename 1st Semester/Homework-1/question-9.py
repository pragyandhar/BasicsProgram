# Question-9: WAP to find the hypotenuse of the triangle, when the base and height are entered by the user

# INPUT AREA
a = int(input("Enter the base: "))
b = int(input("Enter the height: "))
# LOGIC AREA
hypo = ((b**2) + (a**2))**0.5

# DISPLAYING AREA
print("The hypotenuse of the triangle with base", a, "and height", b, "is", hypo)
