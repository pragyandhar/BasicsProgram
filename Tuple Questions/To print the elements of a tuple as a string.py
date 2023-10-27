#To print the elements of a tuple as a string
t = ('1','2','3')
_ = "".join(t)
print(_)

t1 = (1,2,3)
_1 = "".join(map(str,t))
print(_1, type(_1))
