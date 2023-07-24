from flask import render_template, redirect, url_for, request, jsonify, session
from . import app
from .login import isauth
from .models import Product

@app.route("/")
def index():
    products = Product()
    get_products = products.get_record("products")
    get_products = get_products.fetchall()
    if isauth():
        log_in_out = "Logout"
    else:
        log_in_out = "Login"
    return render_template("index.html", datas=get_products, log_condin = log_in_out)

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
    return render_template("admin_dashboard/admin.html")

@app.route("/logout")
def logout_session():
    return redirect(url_for("logout"))