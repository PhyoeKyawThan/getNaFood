from flask import render_template, redirect, url_for, request, jsonify, session
from . import app
from .login import isauth
from .models import Product

@app.route("/")
def index():
    return render_template("index.html")

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

@app.route('/manage/admin')
def admin():
    products = Product()
    get_products = products.get_record("products")
    get_products = get_products.fetchall()
    return render_template("admin_dashboard/admin.html", datas=get_products)