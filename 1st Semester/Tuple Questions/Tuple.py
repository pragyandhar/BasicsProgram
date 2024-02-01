#WAP to unzip the list of tuples into individual tuples

a = [(1,3),(4,6),(3,9)]
box1 = []
box2 = []
for i,j in a:
    box1.append(i)
    box2.append(j)
print(f"elements in box1 are: {box1}")
print(f"elements in box2 are: {box2}")
