from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello Simisola, I\'m Caleb hehe!'

@app.route('/about')

def about_page():
    return 'This is the official About page for my cool Python backend'

@app.route('/greet/<name>')

def greet_user(name):
    return f"Hello there, {name}! Welcome to your personalized page."
