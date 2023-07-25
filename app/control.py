from flask import redirect, render_template, request, jsonify, url_for, session
from . import app
from .models import Product, Order, User
from .login import isauth, user_id

@app.route("/welcome/<response>")
def welcome(response):
    return render_template("welcome.html", message=response)

@app.route("/request/get_item_datas")
def send_data():
    products = Product()
    datas = products.get_record("products")
    datas = datas.fetchall()
    return jsonify(datas)

@app.route("/orders/items")
def order_items():
    if isauth():
        user = session["user"]["username"]
        order = Order()
        user_order = order.get_order_by_user(user)
        user_order = user_order.fetchall()
        return jsonify(user_order)

@app.route("/orders/order_confirm", methods=["POST", "GET"])
def order_confirm():
    if request.method == "POST":
        datas = request.get_json()
        print(datas)
        order_id = datas["order_id"]
        product = Product()
        remain_count = product.get_count(product.get_order_item_name(order_id).fetchone()[0]).fetchone()[0]
        product.close()
        if remain_count < 0:
            message = {
                "message": "Sorry no item left"
            }
            return jsonify(message)
        else:
            order = Order()
            count = order.order_count(order_id)
            order.order_confirm(user_id(), order_id, order.get_order_item_name(order_id).fetchone()[0], count)
            order.close()
            message = {
                "statuc": 200,
                "message": "Order Confirmed and we'll sent to it within 24 hrs"
            }
            return jsonify(message)

@app.route("/add_cart", methods=["POST", "GET"])
def add_cart():
    if request.method == "POST":
        if isauth():
            datas = request.get_json()
            product = Product()
            order_product_detail = product.get_record_by_id(int(datas["order_id"]), "products")
            order_product_detail = order_product_detail.fetchone()
            product.close()
            user = User()
            user_id = user.get_user_id_by_name(session["user"]["username"]).fetchone()[0]
            print(user_id)
            user.close()
            order = Order()
            order_name = order_product_detail[1]
            order.insert(user_id, order_name, datas["count"])
            order.close()
            response = {
                "status": 200,
                "message": "Order added to Cart Check it and Confirm"
            }
            return jsonify(response)
        else:
            return redirect(url_for("login_form"))


@app.route("/orders/order_cancal", methods=["POST", "GET"])
def order_cancal():
    if request.method == "POST":
        if isauth():
            datas = request.get_json()
            print(datas)
            order = Order()
            order.cancal_order(user_id(), datas["order_id"])
            order.close()
            message = {
                "status": 200,
                "message": "Successfully Cancaled"
            }
            return jsonify(message)
        else:
            return redirect(url_for("login_form"))
