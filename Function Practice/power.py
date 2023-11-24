# Write a function to calculate power of a number raised to other. 
def power(a,b):
    c = a**b
    return c

num1 = int(input("Enter the number-1: "))
num2 = int(input("Enter the number-2: "))
out = power(num1,num2)
print(num1,"raised to",num2,"=",out)