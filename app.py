from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stock.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import *


@app.route('/', methods=['GET'])
def shortlist():
    # Retrieve all request arguments, return None if there is no arguments
    country_name = request.args.get('countrycode')
    category_name = request.args.get('Category')
    base_bid = request.args.get('BaseBid')

    # Get all companies based on given country code and category name
    base_target = Company.query.filter(Company.countries.any(name=country_name)).filter(
        Company.categories.any(name=category_name)).all()

    result= []

    # If query returns none send response
    if not base_target:
        return jsonify(response="No Companies Passed from Targeting")

    # Log results
    companies_list = Company.query.all()
    print("BaseTargeting:")
    for company in companies_list:
        if company in base_target:
            if company not in result:
                result.append(company)
            print("{%s, Passed}" % company.name)

        else:
            print("{%s, Failed}" % company.name)

    
    print("Budget Check:")

    for company in companies_list:
        if company in base_target:
            if(company.budget*100 >= company.bid):
                if company not in result:
                    result.append(company)
                print("{%s, Passed}" % company.name)
            else:
                print("{%s, Failed}" % company.name)
        else:
            print("{%s, Failed}" % company.name)


        
    
    print("BaseBid Check:")

    for company in companies_list:
        if company in base_target:
            if(company.bid >= int(base_bid)):
                if company not in result:
                    result.append(company)
                print("{%s, Passed}" % company.name)
            else:
                print("{%s, Failed}" % company.name)
        else:
            print("{%s, Failed}" % company.name)
   
    mincompany = 0
    shortList = result[0]
    for company in result:
        if company.bid > mincompany :
            mincompany=company.bid
            shortList = company

    # shortList.budget -= base_bid
    # session.commit()

    return jsonify(response=shortList.name)


@app.route('/companies', methods=['GET'])
def companies():
    companies_list = Company.query.all()
    result = companies_schema.dump(companies_list)
    return jsonify(result)


if __name__ == '__main__':
    app.debug = True
    app.run()
