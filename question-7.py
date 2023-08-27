# Question-7: WAP to find the area and perimeter of the rectangle, when the sides are entered by the user

# INPUT AREA
a = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
# LOGIC AREA
per = 2*(a+b)
area = a*b
# DISPLAYING AREA
print("The perimeter of the reactangle with length",
      a, "and breath", b, "is", per)
print("The area of the reactangle with length", a, "and breath", b, "is", area)
