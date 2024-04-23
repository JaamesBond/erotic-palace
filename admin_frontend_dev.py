"""The admin dashboard"""
from functools import wraps

from flask import Flask, render_template, request, make_response, redirect, jsonify, url_for, session
import os
from config import CONFIG
from werkzeug.security import check_password_hash
from usersdb import get_user
from admin_methods import *

app = Flask(__name__.split('.')[0], template_folder='/home/matei/PycharmProjects/API_New_New/Templates')
app.config['SECRET_KEY'] = 'Pula mea'


# Custom decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# A method displaying the home page
@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    return render_template("girls/index.html", girls=list_of_girls())


# A methode to import js safely
@app.template_global()
@login_required
def static_include(filename):
    fullpath = os.path.join(app.static_folder, filename)
    with open(fullpath, 'r') as f:
        return f.read()


# A method that adds a new girl
@app.route("/new/", methods=["GET", "POST"])
@login_required
def newgirl():
    if request.method == "GET":
        return render_template("girls/new_girl.html")
    elif request.method == "POST":
        girl = {}
        for key, value in request.form.items():
            if key == "age" or key == "bmi":
                if value.strip():
                    girl[key] = int(value)
                else:
                    girl[key] = None
            else:
                if value.strip():
                    girl[key] = value
                else:
                    girl[key] = None
        """
        girl["name"] = request.form["name"]
        girl["age"] = request.form["age"]
        girl["hair_color"] = request.form["hair_color"]
        girl["phone"] = request.form["phone"]
        girl["boobs"] = request.form["boobs"]
        girl["ass"] = request.form["ass"]
        girl["race"] = request.form["race"]
        girl["bmi"] = request.form["bmi"]
        girl["personality"] = request.form[


"personality"]
        girl["services"] = request.form["services"]
        """
        girl["id"] = add_girl(girl["name"], girl["age"], girl["hair_colour"], girl["phone"], girl["boobs"], girl["ass"], girl["race"], girl["bmi"], girl["personality"], girl["services"])
        return render_template("girls/new_girl.html", girl=girl)

    return make_response("Invalid request", 400)


@app.route("/deletegirl/<int:id>", methods=["GET"])
@login_required
def deletegirl(id):
    delete_girl(id)

    return redirect("/")


@app.route("/editgirl/<int:id>", methods=["GET", "POST"])
@login_required
def editgirl(id):
    if request.method == "GET":
        girl = get_girl_by_id(id)
        return render_template("girls/edit_girl.html", girl=girl)
    elif request.method == "POST":
        girl = {}
        girl["id"] = id
        for key, value in request.form.items():
            if key == "age" or key == "bmi":
                if value.strip():
                    girl[key] = int(value)
                else:
                    girl[key] = None
            else:
                if value.strip():
                    girl[key] = value
                else:
                    girl[key] = None
        update_girl(girl)
        return render_template("girls/edit_girl.html", girl=girl, girl_updated=girl)
    return make_response("Invalid request", 400)


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
            return make_response("Invalid request", 400)


# Route for admin logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host=CONFIG["frontend"]["listen_ip"], port=CONFIG["frontend"]["port"], debug=CONFIG["frontend"]["debug"])
