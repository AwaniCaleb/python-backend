import os

from flask import Flask, redirect, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False) 

    def __repr__(self):
        return f'<User {self.email}>'

@app.route('/')

def hello_world():
    return 'Hello Simisola, I\'m Caleb hehe!'

@app.route('/about')

def about_page():
    return 'This is the official About page for my cool Python backend'

@app.route('/greet/<name>')

def greet_user(name):
    return render_template('profile.html', user_name=name)

@app.route('/submit-data', methods=['POST', 'GET'])

def handle_form():
    if request.method == 'POST':
        data = request.form

        email = data.get('email') or None
        password = data.get('password') or None
        
        if not email or not password:
            return 'Email and Password are required fields.', 400
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(email=email, password=hashed_password)
        
        try:
            db.session.add(new_user)
            db.session.commit()

            return render_template('login-success.html', title='Login Success', user_email=email)
        except Exception as e:
            db.session.rollback()
            return f'An error occurred while saving to the database: {str(e)}', 500

    elif request.method == 'GET':
        return render_template('login.html', title='Login Page')
    else:
        return 'Unsupported request method.'

@app.route('/login', methods=['POST', 'GET'])

def login():
    if request.method == 'POST':
        data = request.form

        email = data.get('email') or None
        password = data.get('password') or None

        if not email or not password:
            return 'Email and Password are required fields.', 400
        
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect('/dashboard')
        else:
            flash('Invalid email or password.', 'error')
            return redirect('/login')
    
    return render_template('login.html', title='Login Page')

@app.route('/logout')

def logout():
    session.pop('user_id', None)
    return redirect('/login')

@app.route('/dashboard')

def dashboard():
    user_id = session.get('user_id')

    if not user_id:
        return redirect('/login')
    
    user = User.query.get(user_id)

    return render_template('dashboard.html', title='Dashboard', user=user)
