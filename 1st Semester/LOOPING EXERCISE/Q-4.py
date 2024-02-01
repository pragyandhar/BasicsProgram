'''
Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''

# n = 5
# for i in range(0, n): #NO OF ROWS
#     for j in range(0, i+1): #NO. OF COLUMNS
#         print("* ", end="")
#     print("\r")
# for i in range(n, 0, -1):
#     for j in range(0, i-1): 
#         print("* ", end="")
#     print("\r")

n = 5
for i in range(0,n):
    for j in range(i+1):
        print("* ", end="")
    print("")
for i in range(n,0,-1):
    for j in range(0,i-1):
        print("* ", end="")
    print("")