import sqlite3

conn = sqlite3.connect("student.db")

c = conn.cursor()

for row in c.execute('SELECT * FROM tblstudent ORDER BY name'):
    print(row)
