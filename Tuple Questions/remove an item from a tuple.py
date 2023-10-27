#WAP to remove an item from a tuple

#Method: First convert the tuple ino a list then removethe item and the again convert it into tuple
a = (1,2,3) #Tuple elements are in integer
b = list(a)
b.remove(3)
c = tuple(b)
print(c)
