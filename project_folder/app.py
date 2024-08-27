from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import mariadb
from models import db, User

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
    
    return redirect(url_for('index'))

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
    # 고객 관리 페이지에 대한 처리를 여기에 작성합니다.
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('customers.html',  customers = customers)

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