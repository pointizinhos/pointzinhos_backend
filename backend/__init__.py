from flask import Flask, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

backend = Flask(__name__)
backend.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://"+os.environ['user']+":"+os.environ['password']+"@"+os.environ['url']+"/"+os.environ['database'] 

db = SQLAlchemy(backend)
ma = Marshmallow(backend)

from .views.basic import basic
from .views.testing import testing

backend.register_blueprint(basic)
backend.register_blueprint(testing)