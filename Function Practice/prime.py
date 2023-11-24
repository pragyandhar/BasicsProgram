# Write a function to check if a number is prime or not.
def primenumber(a):
    for i in range(2,a):
        if a%i == 0:
            print("Not prime number")
            break
    else:
        print("Prime number")

b = int(input("Enter the number: "))
primenumber(b)