import psycopg2

conn = psycopg2.connect("postgresql://postgres:pass123@localhost:5432/books_db")

choice = int(input("Operations\n1 - Add Data\n2 - View All Data"))
cur = conn.cursor()

while True:
    if choice == 1:
        insertQuery = "INSERT INTO books(title, author, year_published, num_pages) VALUES (%s, %s, %s, %s)"
        values = ("A Tale of Two Cities", "Charles Dickens", 1895,450)
        cur.execute(insertQuery, values)
        print("Inserted Successfully")
    elif choice == 2:
        viewQuery = "SELECt * FROM books"
        

conn.commit()
conn.close()