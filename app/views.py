from flask import render_template, redirect, url_for
from . import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return redirect(url_for("index"))

# route for ordered 
@app.route("/orders")
def show_order():
    