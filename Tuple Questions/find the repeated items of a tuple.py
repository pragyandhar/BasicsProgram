#WAP to find the repeated items of a tuple
a = (1,1,2,3,2,3)
reg = []
for i in a:
    if a.count(i)>1 and i not in reg:
        print("The element which is repeated is: ", i)
        reg.append(i)

