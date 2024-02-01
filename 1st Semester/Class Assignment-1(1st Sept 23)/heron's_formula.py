# Question-8: WAP the area of triangle using Heron's formula

# INPUT SECTION
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
# LOGIC SECTION
s = (a+b+c)/2
area = 0.5**(s*((s-a)*(s-b)*(s-c)))

# DISPLAY SECTION
print("The area of triangle with heron's formula is:", area)
