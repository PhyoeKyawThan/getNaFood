from flask import request, jsonify, redirect, url_for
from . import app
from werkzeug.utils import secure_filename
from os import path
from .models import Product, Connect

@app.route('/add_product', methods=["POST", "GET"])
def add_product():
    if request.method == "POST":
        img = request.files["image"]
        product_name = request.form.get("name")
        description = request.form.get("detail")
        price = request.form.get("price")
        count = request.form.get("count")
        file_name = secure_filename(img.filename)
        new_product = Product()
        if file_name:
            img_path = path.join("images", file_name)
            new_product.insert(product_name, description, price, count, img_path)
        else:
            new_product.insert(product_name, description, price, count)
        new_product.close()

        if img:
            if path.exists(path.join(app.config["UPLOAD_FOLDER"], file_name)):
                pass
            else:
                img.save(path.join(app.config["UPLOAD_FOLDER"], file_name))
        response = {
            "status": 200,
            "message": "New Product Added",
            "redirect": "/manage/admin"
        }
        return jsonify(response)

@app.route("/manage/admin/delete/<name>")
def delete_product(name):
    conn = Connect()
    conn.delete_product(name)
    conn.close()
    return redirect(url_for('admin'))

@app.route("/manage/admin/update/<int:id>", methods=["POST", "GET"])
def update_form(id):
    if request.method == "POST":
        datas = request.get_json()
        print(datas)
        response = {
            "status": 200,
            "message": "New Product Added",
            "redirect": "/manage/admin"
        }
        return jsonify(response)