# Class variable is a shared by all instance of the class.
# Instance variable is a variable which is unique to each instance.
class test:
    #class variable
    x = 10
    def __init__(self, val) -> None:
        # Instance variable
        self.ab = val
obj1 = test(20)
obj2 = test(100)
print("Class Variable")
print(obj1.x)
print(obj2.x)
print("\nInstance Variable")
print(obj1.ab)
print(obj2.ab)

print()
obj1.xy = 201
obj1.dy = 214
print("ALL THE INSTANCE VARIABLE OF obj1 IS DISPLAYED BY __dict__")
print(obj1.__dict__)