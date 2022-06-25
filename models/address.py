from countries import db
from sqlalchemy import Column, Integer, String

# Database Models

class Address(db.Model):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    street = Column(String(50))
    number = Column(String(4))
    city = Column(String(30))
    zipcode = Column(String(6))
    city = Column(String(30))
    state = Column(String(20))
    #country_id = Column(Integer)
    description = Column(String(50))
    # has many users
    users = db.relationship('User',backref='address',lazy='dynamic')
    # belongs to country
    country_id = Column(Integer,db.ForeignKey('countries.id'))

    def __init__(self, street, number, city, zipcode, state, country_id):
        street = self.street
        number = self.number
        city = self.city
        zipcode = self.zipcode
        state = self.state
        country_id = self.country_id
        description = self.description

    def save(self):
            db.session.add(self)
            db.session.commit()

    def __repr__(self):
        return f"{self.street} {self.number}, {self.city} ({self.zipcode})"
