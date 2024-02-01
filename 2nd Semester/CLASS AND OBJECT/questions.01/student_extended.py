class Student:
    def __init__(self) -> None:
        self.name = "NA"
        self.age = "NA"
        self.grade = "NA"

    def setDetails(self, name, age):
        self.name = name
        self.age = age

    def getDetails(self):
        return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}"

    def calculate_grade(self, p):
        self.p = p
        if self.p > 95 and self.p < 100:
            self.grade = "O"
        elif self.p > 90 and self.p < 95:
            self.grade = "A+"
        elif self.p > 80 and self.p < 90:
            self.grade = "A"
        elif self.p > 70 and self.p < 80:
            self.grade = "B+"
        elif self.p > 60 and self.p < 70:
            self.grade = "B"
        elif self.p > 50 and self.p < 60:
            self.grade = "C"
        else:
            self.grade = "|FAILED|"

        return f'''
        {self.name}'s grade is {self.grade} as per your percentage {self.p}

        GRADE DISTRIBUTION(OVERALL)
        O --> 95% or above
        A+ --> 90% or above
        A --> 80% or above
        B+ --> 70% or above
        B --> 60% or above
        C --> 50% or above
        '''


# MAIN CODE
stud = Student()
a = str(input("Enter the name: "))
b = int(input("Enter your age: "))
c = int(input("Enter your percentage: "))
stud.setDetails(a, b)
student = stud.calculate_grade(c)
print(student)
