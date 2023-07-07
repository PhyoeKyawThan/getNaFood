from flask import render_template, redirect, request, jsonify, url_for
from . import app
from json import dumps, loads

@app.route("/auth/sign_up/", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        datas = request.get_json()
        print(datas)
        return render_template("index.html")
    else:
        return render_template("sign_up.html")

@app.route("/show/<data>")
def show(data):
    return data