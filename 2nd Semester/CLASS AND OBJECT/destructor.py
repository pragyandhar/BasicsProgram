#DESTRUCTOR: A default method to use to simulate the object deletion

class test:
    def __init__(self) -> None:
        print("This is a constructor")
    def details(self, name):
        self.name = name
    def __del__(self):
        print(f"{self.name} object is deleted")
#DRIVER CODE
obj1 = test()
obj2 = test()
obj2.details("Ravi")
obj1.details("Saket")
del obj2