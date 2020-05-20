from flask import Flask, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

backend = Flask(__name__)
backend.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://"
    + os.environ["USER"]
    + ":"
    + os.environ["PASSWORD"]
    + "@"
    + os.environ["URL"]
    + "/"
    + os.environ["DATABASE"]
)
backend.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(backend)
ma = Marshmallow(backend)

from .views.basic import basic

backend.register_blueprint(basic)

# from .views.credentials import credentials

# backend.register_blueprint(credentials)
