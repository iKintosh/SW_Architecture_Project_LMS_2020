from flask import flash, redirect, request

from LMS import app

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello, World!</h1>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    return f"Hello, {name}!\nYour pass is {password}"
