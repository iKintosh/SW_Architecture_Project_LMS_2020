from flask import flash, redirect, request, url_for

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
    return "<h1>Как они только находят телефоны?!</h1>" \
           '<iframe width="560" height="315" src="https://www.youtube.com/embed/Rqr9tfEAioM" frameborder="0" ' \
           'allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    return redirect(url_for('login2'), code=302)


@app.route('/login2', methods=['GET', 'POST'])
def login2():
    username = request.form.get('username')
    password = request.form.get('password')
    return f"login2 func {username}"
