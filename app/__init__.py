from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("config.py")

from . import views
from . import auth
from .models import User, Order

