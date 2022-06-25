from countries import db, login_manager
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    firstname = Column(String)
    middlename = Column(String)
    lastname = Column(String)
    picture = Column(String)
    hashed_password = Column(String)
    address_id = Column(Integer,db.ForeignKey('addresses.id'))
    country_id = Column(Integer,db.ForeignKey('countries.id'))

    def __init__(self, firstname, middlename, lastname, email, username, picture, hashed_password):
        firstname = self.firstname
        middlename = self.middlename
        lastname = self.lastname
        email = self.email
        username = self.username
        picture = self.picture
        hashed_password = self.hashed_password
        country_id = self.country_id
        address_id = self.address_id

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def __repr__(self):
        return f"UserModel('{self.id}', '{self.username}', '{self.firstname}', '{self.middlename}', '{self.lastname}', '{self.email})"
