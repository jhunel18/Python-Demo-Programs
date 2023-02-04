import sqlite3

conn = sqlite3.connect("student.db")
c = conn.cursor()

name = input("Enter the name to search: ")

c.execute('SELECT * FROM tblstudent WHERE name=?',(name,))
print(c.fetchall())

conn.close()  