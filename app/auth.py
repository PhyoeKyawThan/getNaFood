from flask import render_template, redirect, request
from . import app
from json import dumps, loads

@app.route("auth/sign_up/", methods=["POST", "GET"])
def sign_up(data):
    if request.method == "post":
        datas = request.get_json()
        
    else:
        return render_template("sign_up.html")