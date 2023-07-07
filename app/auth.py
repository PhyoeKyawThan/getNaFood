from flask import render_template, redirect, request, jsonify, url_for, session
from . import app
from json import dumps, loads

@app.route("/sign_up", methods=['POST', 'GET'])
def sign_up():
    if request.method == "POST":
        datas = request.get_json()
        if datas["username"] == session["datas"]["username"]:
            response = {
                "status_code": 200,
                "case": "User already in"
            }
        else:
            session["datas"] = datas
            response = {
                "status_code": 200,
                "case": "Sign_up Successfully"
            }
        return jsonify(response)
    