from flask import render_template, url_for, redirect, request
from . import auth
from flask_login import login_user, login_required, logout_user
from .forms import RegForm, LoginForm
from ..models import User
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
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
        user.save()
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', r_form=form)
