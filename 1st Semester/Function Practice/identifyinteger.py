#Check the elements in list to identify that they are inetgers

#all(): The all() function returns True if all items in an iterable are true, otherwise it returns False.
#any(): The any() function returns True if any item in an iterable are true, otherwise it returns False.

def identify(ls, valid_type):
    return all([valid_type == type(i) for i in ls])

ls = [1,2,3,4,5,7]
re = identify(ls, int)
print(re)