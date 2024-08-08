'''
Write a program to print given pattern by taking input N.

Input Format
The first line contains an integer N.

Constraints
NA

Output Format
Display the pattern as result.

Sample Input
5

Sample Output
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
n = int(input())

for rows in range(n):  # Adjusted the range to start from 0 and include 'n'
    for spaces in range(n - rows - 1):  # Adjusted the range for spaces
        print(' ', end="")
    for asterisks in range(rows + 1):  # Adjusted the range for asterisks
        print("*", end="")
    print()  # Added to move to the next line after each row
