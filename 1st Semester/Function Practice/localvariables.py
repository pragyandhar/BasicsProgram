# Write a Python program to detect the number of local variables declared in a function
'''
IDEA-1:
We can use the co_nlocals() function which returns the number of local variables used by the function to get the desired result.
'''
def local():
    a = 1
    b = 2
    c = "ABCDEFG"

print(local.__code__.co_nlocals)