from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stock.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# return all companies
@app.route('/companies', methods=['GET'])
def companies():
    companies_list = Company.query.all()
    result = companies_schema.dump(companies_list)
    return jsonify(result.data)
