# database models
from app import db
from app import ma

# many_to_many relationships
companies_countries_association = db.Table('companies_countries', db.Model.metadata,
                                           db.Column('company_id', db.Integer, db.ForeignKey('companies.id')),
                                           db.Column('country_id', db.Integer, db.ForeignKey('countries.id'))
                                           )
companies_categories_association = db.Table('companies_categories', db.Model.metadata,
                                            db.Column('company_id', db.Integer, db.ForeignKey('companies.id')),
                                            db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
                                            )


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    budget = db.Column(db.Integer)
    bid = db.Column(db.Integer)
    countries = db.relationship("Country", secondary=companies_countries_association)
    categories = db.relationship("Category", secondary=companies_categories_association)

    def __repr__(self):
        return '<Company %r>' % self.name


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2))

    def __repr__(self):
        return '<Country %r>' % self.name


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return '<Category %r>' % self.name


# schemas for serialize and deserialize objects
class CountrySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


class CompanySchema(ma.Schema):
    countries = ma.Nested(CountrySchema, many=True)
    categories = ma.Nested(CategorySchema, many=True)

    class Meta:
        fields = ('id', 'name', 'budget', 'bid', 'countries', 'categories')


company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
