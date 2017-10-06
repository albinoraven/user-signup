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

    if len(username) < 3 or len(username) > 20:
        user_error = "That's not a valid username"
        
    else:
        user_error = ''

    if ' ' in username:
        user_error = "That's not a valid username"
    else:
        user_error = ''

def validate_password():
    password = request.form['password']

    pass_error = ''

    if len(password) < 3 or len(password) > 20:
        pass_error = "That's not a valid password"
        
    else:
        pass_error = ''

    if ' ' in password:
        pass_error = "That's not a valid password"
    else:
        pass_error = ''

def verify_password():
    password = request.form['password']
    verify = request.form['verify']

    verify_error = ''

    if password == verify:
        verify_error = ''
    else:
        verify_error = "Passwords don't match"


def validate_email():
    email = request.form['email']

    email_error = ''

    if '@' in email and '.' in email:
        email_error = ''
    else: 
        email_error = "That's not a valid email"
        
    if len(email) < 3 or len(email) > 20:
        email_error = "That's not a valid email"
        
    else:
        email_error = ''

    if ' ' in email:
        email_error = "That's not a valid email"
    else:
        email_error = ''


def error_check():
     
    if not user_error and not pass_error and not verify_error and not email_error:
        username = request.form['username']
        return render_template('welcome.html', username=username)
    else:
        return render_template('user_signup.html', user_error=user_error, pass_error=pass_error, verify_error=verify_error, email_error=email_error)
        
    



app.run()