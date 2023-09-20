#INPUT SECTION
a = int(input("Enter the number: "))
i = 1

#LOGIC SECTION
if a < 0:
    print("The factorial is not possible")
elif a == 0:
    print("The factorial is either 0 or 1")
else:
    while a:
        i = i*a
        a = a-1
    print(i)