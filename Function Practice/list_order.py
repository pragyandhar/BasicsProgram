#WAP to craete a list of integers that returns 1 if the list is in ascending order, returns 0 if not sorted and returns -1 if sorted in descending order

#sorted() returns the value whereas sort() doesn't return the value

def sorted_or_not():
    temp = ls[:]
    temp.sort()
    if ls == temp or ls == sorted(ls):
        return "1"
    elif temp == ls[::-1] or ls == sorted(ls,reverse=True):
        return "-1"
    else:
        return "0"

ls = [5,4,3,2,1]
re = sorted_or_not()
print(re)