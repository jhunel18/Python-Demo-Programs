import sqlite3 #import the sqlite3 database


#declare variable to create connection.
conn = sqlite3.connect("student.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS tblstudent(id integer, name text, age integer, address text, contact text, grade real)")

conn.commit()
conn.close()