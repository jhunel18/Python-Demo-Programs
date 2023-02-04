class Employee:
    def __init__(self, name, address, ratePerHour):
        self.name = name
        self.address = address
        self.rateperHour = ratePerHour

    def computeSalary(self, hoursWorked):
        return print("The Employee's salary is "+ str(self.rateperHour * hoursWorked))

        
while True:
    empName = input("Enter the Name: ")
    empAddress = input("Enter the Address: ")
    empRatePerHour= float(input("Enter the Employee's Rate: "))
    hoursWorked = int(input("Enter the number of hours worked: "))

    cashier = Employee(empName, empAddress, empRatePerHour)
    print(cashier.name)
    print(cashier.address)
    print(cashier.rateperHour)
    cashier.computeSalary(hoursWorked)

