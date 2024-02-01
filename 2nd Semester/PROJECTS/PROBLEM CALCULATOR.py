class Calculator:
    def add(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print(f"The sum is [{self.n1}+{self.n2}]")

    def subtract(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print(f"The subtraction is [{self.n1}-{self.n2}]")

    def multiply(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print(f"The multiplication is [{self.n1}*{self.n2}]")

    def division(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print(f"The division is [{self.n1}/{self.n2}]")


# MAIN CODE
a = Calculator()
a.add(2, 3)
a.subtract(8, 4)
a.multiply(3, 4)
a.division(4, 2)
