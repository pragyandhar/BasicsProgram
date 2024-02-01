# Question-13: WAP to find the Simple Interest and the total amount when the Principal, Rate of Interest and Time are entered by the user.

# INPUT SECTION
P = int(input("Enter the Principal Amount you are investing: "))
R = int(input("Enter the Rate of Interest you got: "))
T = int(input("Enter the duration for which you want to invest: "))
# LOGIC SECTION
SI = (P*R*T)/100
Amt = P + SI
# DISPLAY SECTION
print("The Simple Interest you get after", T,
      "years & at", R, "rate of interest is", SI)
print("The amount you get after", T, "years & at", R, "rate of interest is", Amt)
