# INPUT SECTION
P = int(input("Enter the summed number: "))
X = int(input("Enter the xor-ed number: "))

# LOGIC SECTION
for i in range((P//2)+1):
    j = P-i
    if i^j==X:
        #DISPLAY SECTION
        print(i, j)