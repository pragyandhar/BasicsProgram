# INPUT SECTION
a, b = input("Enter two numbers: ").split()
k = input("Enter the threshold: ")
l = int(k)

# LOGIC SECTION
# Logic Subsection-1
x = int(a)
y = int(b)
and_operation = x & y
g = int(and_operation)
or_operation = x | y
h = int(or_operation)
xor_operation = x ^ y
i = int(xor_operation)

# Logic Subsection-2
if g>l and h>l:
    g = 0
    h = 0
    print("The maximum value not exceeding the threshold is: ",i)
elif h>l and i>l:
    h = 0
    i = 0
    print("The maximum value not exceeding the threshold is: ",g)
elif i>l and g>l:
    i = 0
    g = 0
    print("The maximum value not exceeding the threshold is: ",h)