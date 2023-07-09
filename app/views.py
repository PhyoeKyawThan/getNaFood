from flask import render_template, redirect, url_for, request, jsonify, session
from . import app
from .login import isauth

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<response>")
def welcome(response):
    return render_template("welcome.html", message=response)

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

