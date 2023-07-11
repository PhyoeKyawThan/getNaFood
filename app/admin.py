from flask import request, jsonify
from . import app
from werkzeug.utils import secure_filename
from os import path
from .models import Product

@app.route('/add_product', methods=["POST", "GET"])
def order():
    if request.method == "POST":
        img = request.files["image"]
        product_name = request.form.get("name")
        description = request.form.get("detail")
        file_name = secure_filename(img.filename)
        new_product = Product()
        if file_name:
            img_path = path.join("static/images", file_name)
            new_product.insert(product_name, description, img_path)
        else:
            new_product.insert(product_name=product_name, description=description)
        new_product.close()

        if img:
            if path.exists(path.join(app.config["UPLOAD_FOLDER"], file_name)):
                pass
            else:
                img.save(path.join(app.config["UPLOAD_FOLDER"], file_name))
        response = {
            "status": 200,
            "message": "New Product Added"
        }
        return jsonify(response)

    