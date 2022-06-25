from flask_wtf import Form

from wtforms import BooleanField, TextAreaField, StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import InputRequired, Email, Length, AnyOf, EqualTo

class LoginForm(Form):
    email = StringField('Email', validators=[InputRequired(), Length(min=2, max=64)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')


class RegisterForm(Form):
    firstname = StringField('First Name', validators=[InputRequired(), Length(min=2, max=64)])
    middlename = StringField('Middle Name', validators=[Length(min=2, max=64)])
    lastname = StringField('Last Name', validators=[InputRequired(), Length(min=2, max=64)])
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=64)])
    email = StringField('Email', validators=[InputRequired(), Length(min=2, max=64)])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('repeated_password', message="Passwords must match"), Length(min=8, max=128)])
    repeated_password = PasswordField('Repeat the Password', validators=[InputRequired(), EqualTo('password', message="Passwords must match"), Length(min=8, max=80)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Register')
