from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello Simisola, I\'m Caleb hehe!'

@app.route('/about')

def about_page():
    return 'This is the official About page for my cool Python backend'

@app.route('/greet/<name>')

def greet_user(name):
    return render_template('profile.html', user_name=name)
