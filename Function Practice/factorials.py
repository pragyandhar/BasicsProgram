# Write a function to find factorial of a number but also store the factorials calculated in a dictionary.
def fact(a):
    f = 1
    c = {}
    for i in range(1,a+1):
        f *= i
    print("The factorial of the number: ",f)
    new_key = a
    new_value = f
    c[new_key] = new_value
    print("The values stored in dictionary are: ", c)

num1 = int(input("Enter a number: "))
fact(num1)