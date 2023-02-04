import sqlite3

conn = sqlite3.connect("student.db")
c = conn.cursor()

# Create table
c.execute("CREATE TABLE tblstudent (name text,age real)")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
# Insert a row of data
c.execute("INSERT INTO stocks VALUES (name,age)")
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()