# database models
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stock.db"
db = SQLAlchemy(app)


class Company(db.Model):
    CompanyID = db.Column(db.Integer,primary_key=True)
    Budget = db.Column(db.Integer)
    Bid = db.Column(db.Integer)

class Countries(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    CompanyID = db.Column(db.Integer,db.ForeignKey('company.CompanyID'))
    company = db.relationship('Company')
    Country = db.Column(db.String(2))

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    CompanyID = db.Column(db.Integer,db.ForeignKey('company.CompanyID'))
    company = db.relationship('Company')
    Category = db.Column(db.String(10))



if __name__ == '__main__':
    app.run(debug=True)