# Question-11: WAP to find the number of currency notes of each type (Rs. 2000, Rs. 500 and Rs. 100),when the total number of currency notes counted altogether is minimum and there must be at least a 100 rupee note dispensed. The amount to be withdrawn is to be entered by the user.

# INPUT AREA
amt = int(input("Enter the amount: ")) - 100
# LOGIC AREA
two_k = amt//2000
amt = amt - (two_k*2000)

five_h = amt//500
amt = amt - (500*five_h)

one_h = amt//100
# DISPLAYING AREA
print("Notes of 2000: ", two_k)
print("Notes of 500: ", five_h)
print("Notes of 100: ", one_h + 1)
