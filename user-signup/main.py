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
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ''
    verify_error = ''
    pass_error = ''
    email_error = ''


    if len(username) < 3 or len(username) > 20:
        user_error = "That's not a valid username"        
    elif ' ' in username:
        user_error = "That's not a valid username"

    if len(password) < 3 or len(password) > 20:
        pass_error = "That's not a valid password"        
    elif ' ' in password:
        pass_error = "That's not a valid password"      

    if password != verify:        
        verify_error = "Passwords don't match"    

    if not len(email) == 0:
        if not '@' in email or not '.' in email:
            email_error = "That's not a valid email"
        if len(email) < 3 or len(email) > 20:
            email_error = "That's not a valid email"
        if ' ' in email:
            email_error = "That's not a valid email"
    
     
    if not user_error and not pass_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('user_signup.html', user_error=user_error, pass_error=pass_error, verify_error=verify_error, email_error=email_error)
        
    



app.run()