from flask import render_template, redirect, url_for, request, jsonify, session
from . import app
from .login import isauth
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/home/<response>")
def home(response):
    return response

@app.route("/signUp")
def sign_up_form():
    if isauth():
        return redirect(url_for("index"))
    return render_template("sign_up.html")

@app.route("/logIn")
def login_form():
    if isauth():
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("sign_up_form"))