class X:
    def disp(self):
        print('Display from X')
class A(X):
    def disp(self):
        print('Display from A')

class B(X):
    pass

class C(B,A):
    pass

c_obj = C()
c_obj.disp()
print(C.__mro__)
    