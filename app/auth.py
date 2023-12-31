from flask import render_template, redirect, request, jsonify, url_for, session
from . import app
from .models import User
from .login import isauth, check

@app.route("/auth/sign_up", methods=['POST'])
def sign_up():
    if request.method == "POST":
        datas = request.get_json()
        # insert to database
        new_user = (datas["username"], datas["email"], datas["password"])
        user = User()
        users = user.cursor.execute("select username, email, password from user")
        if new_user not in users.fetchall():
            user.insert(new_user)
            session["user"] = datas
            success = "Register Succcess"
            return redirect(url_for("welcome", response=success))
        else:
            response = {
                "status": 409,
                "message": "User Already registered"
            }
            
        return jsonify(response)

@app.route("/auth/login", methods=["POST"])
def login():
    if request.method == "POST":
        datas = request.get_json()
        if isauth():
            return redirect(url_for("index"))
        login_user = (datas["username"], datas["password"])
        user = User()
        users = user.cursor.execute("select username, password from user")
        users = users.fetchall()
        if login_user in users:
            details = user.cursor.execute(f"select * from user where username = '{datas['username']}' and password = '{datas['password']}'")
            details = details.fetchone()
            exist_user = {
                "username": details[1],
                "email": details[2],
                "password": details[3]
            }
            session['user'] = exist_user
            success = f"welcome back Mr.{login_user[0]}"
            return redirect(url_for("welcome", response=success))
        else:
            response = {
                "status": 404,
                "message": "User Not Found and Sign up"
            }
            return jsonify(response)

@app.route('/auth/admin/login', methods=["POST", "GET"])
def admin_login():
    if "admin" not in session:
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            if check(username, password):
                session["admin"] = {
                    "username": username,
                    "password": password
                }
                return redirect(url_for("admin"))
            else:
                message = "Username or password wrong, try again!"
                return render_template("admin_dashboard/login.html", alert=message)
        else:
            return render_template("admin_dashboard/login.html")
    else:
        return redirect(url_for("admin"))

@app.route("/auth/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

