import sqlite3

conn = sqlite3.connect("student.db")

c = conn.cursor()

id = int(input("Enter the id: "))
stud_name = input("Enter your name: ")
stud_age = int(input("Enter your age: "))
stud_address = input("Enter you address: ")
stud_contact = input("Enter your contact ")
stud_grade = float(input("Enter your grade: "))

#INSERT 
c.execute("""
INSERT INTO tblstudent(id, name,age, address, contact, grade)
VALUES(?,?,?,?,?,?)
""", (id, stud_name,stud_age,stud_address,stud_contact,stud_grade))
print("Inserted Data Successfully")

conn.commit()
conn.close()