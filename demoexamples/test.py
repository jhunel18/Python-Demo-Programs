class Student:

    def __init__(self, id, firstName, lastName, course, tuitionFees):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.course = course
        self.tuitionFees = tuitionFees
    
    def ComputeTuition(self,units):

        return print(units * self.tuitionFees)


student1 = Student(1, "Jhunel", "Penaflorida", "BSIT", 12)
print(student1.id)
print(student1.firstName)
print(student1.lastName)
print(student1.course)
student1.ComputeTuition(24)
