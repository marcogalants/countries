from countries import db
from sqlalchemy import Column, Integer, String

# Database Models

class Country(db.Model):
    __tablename__ = "countries"
    id = Column(Integer,primary_key=True)
    name = Column(String(30), unique=True)
    topLevelDomain = Column(String(8))
    alpha2Code = Column(String(5))
    alpha3Code = Column(String(5))
    callingCodes = Column(String(5))
    flag = Column(String(48))
    population = Column(Integer())
    capital = Column(String(32))
    timezones = Column(String(16))
    region = Column(String(32))
    nativeName = Column(String(30))
    numericCode = Column(Integer())
    subregion = Column(String(20))
    currencies = Column(String(32))
    borders = Column(String(48))
    gini = Column(Integer())
    users = db.relationship('User',backref='country',lazy='dynamic')
    addresses = db.relationship('Address',backref='country',lazy='dynamic')

    def __init__(self,name,topLevelDomain,alpha2Code,alpha3Code,callingCodes,region,capital,flag="defaultflag.png"):
        name = self.name
        topLevelDomain = self.topLevelDomain
        alpha2Code = self.alpha2Code
        alpha3Code = self.alpha3Code
        callingCodes = self.callingCodes
        flag = self.flag
        currencies = self.currencies
        capital = self.capital
        region = self.region

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"{self.name} ({self.topLevelDomain}) ({self.alpha2Code}) ({self.alpha3Code}) ({self.callingCodes}) is located in {self.region}. Capital is {self.capital}"
