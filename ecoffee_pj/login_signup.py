import os
import sys
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from ecoffee_database_setup import Base, User as UserModel, Post
from werkzeug.utils import secure_filename


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine('mysql+pymysql://root:1108@localhost/ecoffee_db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app.secret_key = 'asdsadadasdamsasdklfaskdl'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = session.query(UserModel).filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return render_template('mainpage.html', username=username)
        else:
            return render_template('login.html', message="로그인 실패. 다시 시도하세요.")
        
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            return render_template('signup.html', message="비밀번호가 일치하지 않습니다. 다시 시도하세요.")
        
        try:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = UserModel(username=username, password=hashed_password, email=email)
            session.add(new_user)
            session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            session.rollback()
            return f"회원가입 중 오류가 발생했습니다: {str(e)}"
    
    return render_template('signup.html')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)
