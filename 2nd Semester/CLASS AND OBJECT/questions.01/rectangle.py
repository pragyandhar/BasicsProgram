class shape:
    def __init__(self, side1, side2) -> None:
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2*(self.side1 + self.side2)


class Rectangle(shape):
    def __init__(self, l, b) -> None:
        super().__init__(l, b)


class Square(shape):
    def __init__(self, side) -> None:
        super().__init__(side, side)


# MAIN CODE
l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
s = int(input("Enter any side of the square: "))
rec = Rectangle(l, b)
sqr = Square(s)
area1 = rec.area()
area2 = sqr.area()
peri1 = rec.perimeter()
peri2 = sqr.perimeter()
print(f"Area of Rectangle for given dimensions {l} and {b} are {area1}")
print(f"Area of Square for given side {s} is {area2}")
print(f"Area of Rectangle for given dimensions {l} and {b} are {peri1}")
print(f"Area of Square for given side {s} is {peri2}")
