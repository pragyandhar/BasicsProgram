class Task:
    def __init__(self, val) -> None:
        self.val = val

    def get(self):
        return self.val

    def set(self, v):
        self.val = v


obj1 = Task(20)
obj2 = Task(30)
obj1.val = 100
print(obj1.get())

# isinstance(): it is a method which checks an object is of a particular class or not.
# dir(): it displays all the pre-defined variables inside a class
# repr(): it displays the type of value directly. If the class is string then the output will be displayed as "123" instead of 123.

print(isinstance(obj1, Task))
x = "123"
y = '''hello
python'''
print(repr(x), type(x))  # "123" <class 'str'>
print(repr(y), type(y))  # hello\nworld <class 'str'>


# "__dict__": to display all the attributes for an object
print(obj1.__dict__)
# "__setattr__": it sets the value of the object.
setattr(obj1, "val1", 1200)
print(obj1.__dict__)
# "__getattr__": it returns the value of the set value
out = getattr(obj1, "val1")
print(out)
# "__delattr__": to delete an attribute
delattr(obj1, "val")
print(obj1)
