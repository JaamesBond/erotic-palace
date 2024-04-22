from functools import wraps

from flask import Flask, render_template, request, make_response, redirect, jsonify, url_for, session
import os
from config import CONFIG
from werkzeug.security import check_password_hash, generate_password_hash
from usersdb import add_user, get_user

app = Flask(__name__.split('.')[0], template_folder='/home/matei/PycharmProjects/Users_API/Templates')
app.config['SECRET_KEY'] = 'Pula mea'


# Custom decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')


# Route for signup (user registration)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists
        if get_user(username):
            return "Username already exists. Please choose a different username."

        # Add new user to the database
        add_user(username, password)
        return redirect(url_for('index'))  # Redirect to login page after signup

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']

        user = get_user(username)

        if user and check_password_hash(user[2], password):
            # Successful login
            session['username'] = username  # Store the username in session
            return redirect(url_for('index'))
        else:
            return "Username or password incorrect"


# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host=CONFIG["frontend"]["listen_ip"], port=CONFIG["frontend"]["port"], debug=CONFIG["frontend"]["debug"])
