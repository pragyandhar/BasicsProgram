class Person:
    def speak(self):
        print("Person Speaking")


class Dog(Person):
    def bark(self):
        print("Dog Barking")


# obj1 = Person()
obj1 = Dog()
obj1.bark()
obj1.speak()


class Parent:
    # members of Parents
    pass


class Child(Parent):
    # members of Child
    pass
