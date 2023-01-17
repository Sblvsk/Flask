from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserRegisterForm(FlaskForm):
    first_name = StringField('first_name')
    last_name = StringField('last_name')
    email = StringField('email', [validators.DataRequired(), validators.Email()])
    password = StringField('password', [validators.DataRequired(), validators.EqualTo('confirm_password')])
    confirm_password = PasswordField('confirm_password', [validators.DataRequired()])
    submit = SubmitField('register')
