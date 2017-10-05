from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('user_signup.html')

@app.route("/", methods=['POST'])
def validate_username():
    username = request.form['username']

    user_error = ''

    if len('username') < 3 or len('username') > 20:
        user_error = "That's not a valid username"
        
    else:
        user_error = ''

def validate_password():
    password = request.form['password']

    pass_error = ''

    if len('password') < 3 or len('password') > 20:
        pass_error = "That's not a valid password"
        
    else:
        pass_error = ''

def validate_email():
    email = request.form['email']

    email_error = ''
        
        
    

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)







app.run()