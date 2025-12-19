from flask import Flask, render_template, request

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

@app.route('/submit-data', methods=['POST', 'GET'])

def handle_form():
    if request.method == 'POST':
        return 'Form submitted successfully!'
    elif request.method == 'GET':
        return render_template('login.html', title='Login Page')
    else:
        return 'Unsupported request method.'
