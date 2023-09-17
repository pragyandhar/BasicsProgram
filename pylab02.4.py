# INPUT SECTION
a = int(input("Enter the number: "))
# LOGIC SECTION-1
w = len(bin(a))-2
for i in range(a+1):
    x = bin(i)[2:]
    print(f"{x:>{w}}")
print("\r")
# LOGIC SECTION-2
y = len(bin(a)[2:])
for j in range(a+1):
    x = bin(j)[2:]
    print(" "*(w-len(x))+x)