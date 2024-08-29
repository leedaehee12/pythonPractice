from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import pandas as pd
import mariadb
from models import db, User
from models import Customers

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://pythonUser:1234@localhost:3306/pythonpractice'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

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
        
        return redirect(url_for('customers'))
    
    return render_template('add.html')

# 엑셀 파일 업로드를 위한 라우트
@app.route('/upload_customers', methods=['GET', 'POST'])
def upload_customers():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and file.filename.endswith('.xlsx'):
            try:
                # 엑셀 파일을 읽어서 데이터프레임으로 변환
                df = pd.read_excel(file)

                # 데이터베이스에 고객 추가
                for index, row in df.iterrows():
                    new_customer = Customers(
                        name=row['Name'],
                        email=row['Email'],
                        phone=row['Phone']
                    )
                    db.session.add(new_customer)

                db.session.commit()
                flash('Customers uploaded successfully!')
                return redirect(url_for('customers'))

            except Exception as e:
                flash(f'An error occurred: {e}')
                return redirect(request.url)
        else:
            flash('Invalid file format. Please upload an Excel file.')
            return redirect(request.url)

    return render_template('upload_customers.html')

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
        
        return redirect(url_for('customers'))
    
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
    
    return redirect(url_for('customers'))

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

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.route('/test')
def test():
    users = User.query.all()
    return f"Total Users: {len(users)}"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash('계정이 성공적으로 생성되었습니다!')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('로그인 성공!')
            return redirect(url_for('index'))
        else:
            flash('이메일이나 비밀번호가 잘못되었습니다.')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('로그아웃되었습니다.')
    return redirect(url_for('login'))

# @app.route('/')
# @login_required
# def index():
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM customers")
#     customers = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return render_template('index.html', customers = customers)

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/customers')
@login_required
def customers():
    query = request.args.get('query', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    conn = connect_db()
    cursor = conn.cursor()

    if query:
        search_query = f"%{query}%"
        cursor.execute("""
            SELECT * FROM customers 
            WHERE name LIKE ? OR email LIKE ? OR phone LIKE ?
            LIMIT ? OFFSET ?
        """, (search_query, search_query, search_query, per_page, (page - 1) * per_page))
        customers = cursor.fetchall()
        cursor.execute("SELECT COUNT(*) FROM customers WHERE name LIKE ? OR email LIKE ? OR phone LIKE ?", (search_query, search_query, search_query))
        total = cursor.fetchone()[0]
    else:
        cursor.execute("SELECT * FROM customers LIMIT ? OFFSET ?", (per_page, (page - 1) * per_page))
        customers = cursor.fetchall()
        cursor.execute("SELECT COUNT(*) FROM customers")
        total = cursor.fetchone()[0]

    cursor.close()
    conn.close()
    
    num_pages = (total + per_page - 1) // per_page  # 총 페이지 수

    return render_template('customers.html', customers=customers, page=page, num_pages=num_pages, query=query)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 데이터베이스 테이블 생성
    app.run(debug=True)
    
    