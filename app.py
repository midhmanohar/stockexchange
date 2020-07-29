from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stock.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import *



@app.route('/companies', methods=['GET'])
def companies():
    companies_list = Company.query.all()
    result = companies_schema.dump(companies_list)
    return jsonify(result)



if __name__ == '__main__':
    app.debug = True
    app.run()

