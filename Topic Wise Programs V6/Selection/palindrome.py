# Q: Write a program to find whether a given string or number is palindrome or not
test_number = 922922929
if str(test_number) == str(test_number)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")