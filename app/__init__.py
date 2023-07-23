from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config.from_pyfile("config.py")

from . import views
from . import auth
from . import control
from . import admin

