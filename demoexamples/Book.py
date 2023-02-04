class Employee:

    def __init__(self, name, address, rateperHour):
        self.name = name
        self.address = address
        self.rateperHour = rateperHour
    
    def computeSalary(self, hoursWorked):
        salary = self.rateperHour * hoursWorked
        return print(salary)
    

#instatiation - creating an object

emp1 = Employee("Jhunel", "Unisan, Quezon",186.90)
print(emp1.name)
print(emp1.address)
print(emp1.rateperHour)
emp1.computeSalary(200)

emp2 = Employee("Jose", "Agdangan, Quezon", 190.45)
print(emp2.name)
print(emp2.address)
print(emp2.rateperHour)
emp2.computeSalary(164)


