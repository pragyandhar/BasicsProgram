'''When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no
upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True'''

a = int(input("Enter the number of cigars: "))
b = bool(input("Weekend? (True/False): "))
if b == False and a>40 or a<60:
    print("True")
elif b == True and a>60 or a<40:
    print("True")
else:
    print("False")
