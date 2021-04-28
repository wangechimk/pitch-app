from flask import render_template, url_for, redirect, request
from . import auth
from flask_login import login_user, login_required, logout_user
from .forms import RegForm, LoginForm
from ..models import User
from .. import db
from ..email import mail_message


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    print(form.username.data, 'username')
    print(form.validate(), 'validate')
    print(form.is_submitted(), 'is submitted')
    if form.validate_on_submit():
        print('niko hapa')
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')
    return render_template('auth/login.html', loginform=LoginForm())


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        user.save_u()
        # mail_message("Welcome to Pitch-App", "email/welcome_user", user.email, user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', r_form=form)
