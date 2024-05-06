class X:
    def disp(self):
        print('Display from X')
class A(X):
    def disp(self):
        print('Display from A')
        super().disp()

class B(X):
    def disp(self):
        print('Display from B')
        super().disp()
class C(B,A):
    def disp(self):
        print('Display from C')
    pass
c_obj = C()
c_obj.disp()
print(C.__mro__)
    