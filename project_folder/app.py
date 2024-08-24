from flask import Flask, render_template, request, redirect, url_for
import mariadb

app =Flask(__name__)

#데이터 베이스 연결
def connect_db():
    try:
        conncetion = mariadb.connect(
            user = "pythonUser",
            password = "1234",
            host = "localhost",
            port = 3306,
            database = "pythonpractice"   
        )
        return conncetion
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return None

#메인페이지(고객목록 보기)
@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', customers = customers)

#고객 추가 페이지 및 처리
@app.route('/add', methods = ['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, email, phone) VALUES (?,?,?)", (name, email, phone))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('add.html')

#고객 정보 수정 페이지 및 처리
@app.route('/edit/<int:id>', methods = ['GET', 'POST'])
def edit_customer(id):
    conn = connect_db()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        cursor.execute("UPDATE customers SET name = ?, email = ?, phone = ? WHERE id = ?", (name, email, phone, id))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('index'))
    
    cursor.execute("SELECT * FROM customers WHERE id = ?", (id,))
    customer = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return render_template('edit.html', customer = customer)

#고객 삭제처리
@app.route('/delete/<int:id>')
def delete_customer(id):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM customers WHERE id = ?", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug = True)
        
    