from flask import render_template, redirect, request, jsonify, url_for, session
from . import app, views
from .models import User
from .login import isauth

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
            return redirect(url_for("index"))
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
        if login_user in users:
            return redirect(url_for("index"))
        else:
            response = {
                "status": 404,
                "message": "User Not Found and Sign UP"
            }
            return jsonify(response)
