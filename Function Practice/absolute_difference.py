#If the common difference between the elements of the items of a list is increasing then return true else return false

def strict_difference(ls):
    a = []
    for i in range(0,len(ls)-1):
        diff = abs(ls[i]-ls[i+1])
        a.append(diff)
    return sorted(a) == a

arr = [1,2,5,-1]
re = strict_difference(arr)
print(re)