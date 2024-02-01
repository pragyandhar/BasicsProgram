#WAP to find the python function to find the union between the two list of integers

def union(ls1,ls2):
    c = []
    for i in ls2:
        if i not in ls1:
            c.append(i)
            ls = ls1+c
    return ls
def intersection(ls1,ls2):
    c = []
    for i in ls2:
        if i in ls1:
            c.append(i)
    return c
    
def symmetric_difference(ls1,ls2):
    a = union(ls1,ls2)
    b = intersection(ls1,ls2)
    for i in union(ls1,ls2):
        if i in b:
            a.remove(i)
    return a

arr1 = [1,2,3,5,5]
arr2 = [2,5,90]

re1 = union(arr1, arr2)
re2 = intersection(arr1,arr2)
re3 = symmetric_difference(arr1, arr2)
print(re1)
print(re2)
print(re3)