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
        product = Product()
        if(str(list(datas.values())[0])):
            update_data = (list(datas.keys())[0], f"'{list(datas.values())[0]}'")
            product.update_product(id, update_data)
        else:
            update_data = (list(datas.keys())[0], list(datas.values())[0])
            product.update_product(id, update_data)
        product.close()
        change_data = list(datas.values())[0]
        response = {
            "status": 200,
            "message": "Updated datas",
            "updated_data": change_data
        }
        print(response)
        return jsonify(response)

@app.route("/manage/admin/update/product_image/<int:id>", methods=["POST", "GET"])
def img_update(id):
    if request.method == "POST":
        img = request.files["img"]
        filename = secure_filename(img.filename)
        if img:
            if path.exists(path.join(app.config["UPLOAD_FOLDER"], filename)):
                product = Product()
                img_path = path.join("images", filename)
                update_data = ("product_img", f"'{img_path}'")
                product.update_product(id, update_data)
                product.close()
                response = {
                    "status": 403,
                    "message": "File already exists",
                    "updated_data": img_path
                }
            else:
                product = Product()
                img_path = path.join("images", filename)
                update_data = ("product_img", f"'{img_path}'")
                product.update_product(id, update_data)
                product.close()
                img.save(path.join(app.config["UPLOAD_FOLDER"], filename))
                response = {
                    "status": 200,
                    "message": "Image Updated",
                    "updated_data": img_path
                    }
        return jsonify(response)