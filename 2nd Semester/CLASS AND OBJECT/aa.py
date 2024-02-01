class employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
    def getDetails(self):
        return f'''
        Name : {self.name}
        Salary: {self.salary}
        '''
    def update_sal(self, new_sal):
        self.salary = new_sal

emp1 = employee("Ravi", "200000")
emp1.update_sal(10000000)
print(emp1.getDetails())