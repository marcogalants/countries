
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path as path
from os import environ as environ
import re


app = Flask(__name__)
app.secret_key = environ['SECRET_KEY']
basedir = path.abspath(path.dirname(__file__))

#### SQLITE3 DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, 'country.db')
###############

# POSTGRESQL DB
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
migrate = Migrate(app, db)

import users_view, countries_view, addresses_view

app.config['DEBUG'] = 1

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    db.init_app()
    app.run(port=environ['FLASK_PORT'], debug=environ['FLASK_DEBUG'])

