class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember : {})'.format(self.name))

    def tell(self):
        print('Name : "{}" Age: "{}"'.format(self.name, self.age),)


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher : {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary : "{:d}"'.format(self.salary))

class Student(SchoolMember):

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student : {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:f}"'.format(self.marks))

while True:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    salary = input("Enter your salary")

    t = Teacher(name, age, salary)
    
    t.tell()