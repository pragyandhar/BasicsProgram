str1 = input("::::")
str3 = str1.lower()
str2 = str3[::-1]
print("Reversed String: ", str2)
if str3 == str2:
    print("Palindrome")
else:
    print("Not Palindrome")
