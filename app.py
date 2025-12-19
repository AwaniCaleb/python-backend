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
