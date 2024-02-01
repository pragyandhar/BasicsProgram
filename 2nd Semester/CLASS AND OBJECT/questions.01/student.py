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


# MAIN CODE
if __name__ == "__main__":
    stud = Student()
    stud.setDetails("Ravi", 20)
    student = stud.getDetails()
    print(student)
