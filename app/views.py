from flask import render_template, redirect, url_for, request, jsonify
from . import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return redirect(url_for("index"))

@app.route("/signUp")
def sign_up_form():
    return render_template("sign_up.html")