import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

        return render_template('login-success.html', title='Login Success', user_email=email)
    elif request.method == 'GET':
        return render_template('login.html', title='Login Page')
    else:
        return 'Unsupported request method.'
