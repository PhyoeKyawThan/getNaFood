from flask import render_template, redirect, url_for, request, jsonify, session
from . import app
from .login import isauth, check, admin_exist
from .models import Product, Order

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

@app.route("/orders")
def view_user_order():
    return render_template("orders.html")

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
    if admin_exist():
        return render_template("admin_dashboard/admin.html")
    else:
        return redirect(url_for("admin_login"))



@app.route("/logout")
def logout_session():
    return redirect(url_for("logout"))