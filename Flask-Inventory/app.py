from flask import Flask, render_template, url_for, request, redirect
import psycopg2

app = Flask(__name__)

#connection to the database
conn = psycopg2.connect("postgresql://postgres:pass123@localhost:5432/inventory_db")

@app.route('/')
def index():

    cur = conn.cursor()
    viewQuery="SELECT * FROM products ORDER BY qty"
    cur.execute(viewQuery)
    data = cur.fetchall()

    return render_template("index.html", products = data)

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/add/add_data/', methods = ['POST','GET'])
def add_data():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        qty = request.form['qty']
        
        #code to save
        cur = conn.cursor()
        insertQuery = "INSERT INTO products(name,description,qty) VALUES (%s,%s,%s)"
        productValues = (name, description, qty)

        cur.execute(insertQuery,productValues)
        conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<string:id>', methods = ['GET'])
def delete(id):
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id = %s", (id,))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods =['GET'])
def update(id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE id = %s",(id,))
    data = cur.fetchone()

    return render_template('update.html', products = data)

@app.route('/update/update_data/', methods = ['POST','GET'])
def update_data():
    if request.method == 'POST':
        id = request.form['id']
        name=request.form['name']
        description = request.form['description']
        qty = request.form['qty']

        cur = conn.cursor()
        updateQuery ="UPDATE products SET name = %s, description = %s, qty = %s WHERE id = %s"
        newValues = name, description,qty, id
        cur.execute(updateQuery, newValues)
        conn.commit()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port = 80, debug= True)