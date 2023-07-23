from flask import redirect, render_template, request, jsonify
from . import app
from .models import Product

@app.route("/welcome/<response>")
def welcome(response):
    return render_template("welcome.html", message=response)

@app.route("/request/get_item_datas")
def send_data():
    products = Product()
    datas = products.get_record("products")
    datas = datas.fetchall()
    return jsonify(datas)

