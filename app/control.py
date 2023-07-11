from flask import redirect, render_template, request
from . import app

@app.route("/welcome/<response>")
def welcome(response):
    return render_template("welcome.html", message=response)

