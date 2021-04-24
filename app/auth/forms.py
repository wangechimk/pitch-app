from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from ..models import User


def valid_username(data_field):
    if User.query.filter_by(username=data_field.data).first():
        raise ValidationError('The username you entered has already been taken')


def valid_email(data_field):
    if User.query.filter_by(email=data_field.data).first():
        raise ValidationError('An account with that email already exist')


class RegForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    username = StringField('Enter Your Username', validators=[Required()])
    password = PasswordField('Password',
                             validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')
