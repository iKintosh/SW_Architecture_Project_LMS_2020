from flask import flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from LMS.models import User

from LMS import app


@app.route('/')
def start_page():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('start_page'))
    user = User.query.filter_by(email=request.form.get('email'))
    if user is None or not user.check_password(request.form.get('password')):
        flash('Invalid username or password')
    login_user(user, remember=True)
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
        next_page = url_for('index')
    return redirect(next_page)


@app.route('/invite', methods=['GET', 'POST'])
def invite():
    if current_user.is_authenticated:
        return redirect(url_for('start_page'))
    user = User.query.filter_by(verification_code=request.form.get('verification_code'))
    if user is None or user.is_registered is True:
        flash('Invalid username or password')
    user
    db.session.add(user)
    db.session.commit()
    flash('Congratulations, you are now a registered user!')
    return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
