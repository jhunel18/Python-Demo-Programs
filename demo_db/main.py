import sqlite3

conn = sqlite3.connect("student.db")
c = conn.cursor()
while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:

        c.execute("CREATE TABLE IF NOT EXISTS tblstudent(name text, age integer, address text, contact text, grade real)")
        conn.commit()
        conn.close()

    elif choice == 2:

        #INSERT 
        stud_name = input("Enter your name: ")
        stud_age = int(input("Enter your age: "))
        stud_address = input("Enter you address: ")
        stud_contact = input("Enter your contact ")
        stud_grade = float(input("Enter your grade: "))

        
        c.execute("""
        INSERT INTO tblstudent(name,age, address, contact, grade)
        VALUES(?,?,?,?,?)
        """, (stud_name,stud_age,stud_address,stud_contact,stud_grade))
        print("Inserted Data Successfully")

        conn.commit()
        conn.close()

    elif choice == 3:

        #view one item
        name = input("Enter the name to search: ")
        c.execute('SELECT * FROM tblstudent WHERE name=?',(name,))
        print(c.fetchall())
        conn.close()
    else:
        print("Invalid Input")