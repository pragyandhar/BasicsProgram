# Question-14: WAP to find the compound interest and the total amount when the Principal Amount, Rate of Interest and Time is enetered by the User

# INPUT AREA
P = float(input("Enter the Principal Amount: "))
R = int(input("Enter the Rate of Interest: "))
T = int(input("Enter the Time required: "))

# LOGIC AREA
Amt = P*((1+(R/100))**(T))
CI = P-Amt

# DISPLAY AREA
print("The Amount after", T, "Years will be", Amt)
print("The Compound Interest at", R, "%", "Rate of Interest is=", CI)
