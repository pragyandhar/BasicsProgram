#WAP to add item in a tuple
t = (1,2)
item = int(input("No. please: "))
t = t + (item,) #t + (item,) hai to item ko bracket me likhna parega aur agar augumented expression ho to brackets ki zarurat nhi hai
print(t)

t = (1,2)
lst = list(t)
lst.append(int(input("Number: ")))
t = tuple(lst)
print(t)
