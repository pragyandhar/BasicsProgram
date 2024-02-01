# Question-10: Develop a program that calculates the volume of a cylinder with height and radius to be entered by the user
import math as m
# INPUT SECTION
r = int(input("Enter the radius of cylinder: "))
h = int(input("Enter the height of cylinder: "))

# LOGIC SECTION
vol = m.pi*(r**2)*h

# DISPLAY SECTION
print("The volume of cylinder with height as",
      h, "and radius as", r, "is:", vol)
