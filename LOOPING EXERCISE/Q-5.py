# Write a Python program that accepts a word from the user and reverses it.

a = "ABCD"

for i in range(len(a)-1,-1,-1):
    # print(a.replace([i],[1-i]))
    print(a[i], end="")
    # print("")
    