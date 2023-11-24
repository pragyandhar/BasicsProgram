# Write a function to calculate area and perimeter of a rectangle.
def area(x,y):
    area = x*y
    print("The area of the rectangle is: ", area)
def perimeter(c,d):
    perimeter = 2*(c+d)
    print("The perimenter of the rectangle is: ", perimeter)

a = int(input("Enter length: "))
b = int(input("Enter breadth: "))
area(a,b)
perimeter(a,b)

# Write a function to calculate area and circumference of a circle.
from math import *
def area(y):
    area = pi*y**2
    print("The area of the circle is: ", area)
def perimeter(c):
    perimeter = 2*pi*c
    print("The perimenter of the rectangle is: ", perimeter)

a = int(input("Enter radius: "))
area(a)
perimeter(a)