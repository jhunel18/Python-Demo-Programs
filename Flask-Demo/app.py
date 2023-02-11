from flask import Flask, render_template, url_for, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("postgresql://postgres:pass123@localhost:5432/books_db")

#postgresql://, the connection scheme
# postgres:root, user + password (we use the default postgres user here)
# @localhost:5432, the hostname and its port
# /postgres, which database we connect to (again, the default one)

@app.route('/')
def index():

   cur = conn.cursor()
   cur.execute("SELECT * FROM books")
   data = cur.fetchall()
   
   return render_template('index.html', books = data)
   
@app.route('/insert')
def insert():
   return render_template('insert.html')

#Used to insert the data
@app.route('/insert/insert_data/', methods = ['POST','GET'])
def insert_data():
   if request.method == "POST":
      title = request.form['title']
      author = request.form['author']
      year_published = request.form['year_published']
      num_pages = request.form['num_pages']

      cur = conn.cursor()
      insertQuery = "INSERT INTO books(title, author, year_published, num_pages) VALUES (%s, %s, %s, %s)"
      values = (title, author, year_published, num_pages)
      cur.execute(insertQuery, values)
      print("Data Inserted Successfully.")
      conn.commit()
      

   return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(host = "127.0.0.1", port = 80, debug=True)