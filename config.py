from flask import Flask
import bcrypt
from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify, request

from pymongo import MongoClient

from flask_jwt_extended import JWTManager, jwt_required, create_access_token

import werkzeug.exceptions
from flask_mongoengine import MongoEngine

# from flask_mongoengine import MongoEngine


app = Flask(__name__)


client = MongoClient('mongodb+srv://kaushal:rmituniversity@cluster0.zkw6e.mongodb.net/application_db?retryWrites=true&w=majority')

db = client.get_default_database()

items = db['Items']
zhiffy = db['Zhiffy']
cart = db['Cart']
order = db['Order']

index_name = 'my_index'
# items.create_index(index_name, unique=False)
# zhiffy.create_index(index_name, unique=False)
# cart.create_index(index_name, unique=False)
# order.create_index(index_name, unique=False)
# mongo = PyMongo(app)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/application_db"

app = Flask(__name__)
jwt = JWTManager(app)
app.config["MONGO_URI"] = "mongodb+srv://kaushal:rmituniversity@cluster0.zkw6e.mongodb.net/application_db?retryWrites=true&w=majority"
app.config["JWT_SECRET_KEY"] = "ACCESS_KEY_999"
mongo = PyMongo(app)

