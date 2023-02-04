import sqlite3

# conn = sqlite3.connect("student.db")
# c = conn.cursor()

# #name = input("Enter the name to search: ")
# name = input("Enter the name you want to change: ")

# query= "UPDATE tblstudent SET name = ?"
# c.execute(query,(name,))

# getAllData = c.execute("SELECT * FROM tblstudent order by name")

# for row in getAllData:
#     print(row)
    
# conn.commit()
# conn.close()  

def create_connection(student):

    conn = None
    conn = sqlite3.connect(student)
    
    return conn

def update(conn, task):
    sql = '''UPDATE tblstudent SET id = ?, name = ?, age = ?, contact = ?, address = ?, grade = ?
    where id = ?'''

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def main():
    database = ("student.db")
    conn = create_connection(database)
    with conn:
        update(conn,(1, "James", 25, "0912345678910", "Plaridel", 2.75, 1))

if __name__ == '__main__':
    main()