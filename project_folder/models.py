from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.String(150), nullable=False)

    # 비밀번호 설정시 해시 생성
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # 비밀번호 검증
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    

class Customers(db.Model):
    __tablename__ = 'customers'  # 테이블 이름을 'customers'로 지정
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    
    def __init__(self, name, email, phone) :
        self.name = name
        self.email = email
        self.phone = phone