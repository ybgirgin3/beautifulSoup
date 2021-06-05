from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db

# never store a password as a plain text
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        
        else:
            flash('Email doesnot exist.', category='error')


    return render_template("login.html", text="Testing", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')



        if len(email) < 4:
            flash('email must be greater than 4 characters', category='error')
        elif len(first_name) < 2:
            flash('first name must be greater than 1 char', category='error')

        elif password1 != password2:
            flash('password does not match', category='error')
        elif len(password1) < 7:
            flash('password fazla olsun amk', category='error')
        else:
            # kullanıcıyı veritabanına ekle
            
            # define user
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))

            # add user to database
            db.session.add(new_user)
            db.session.commit()
            # bu kadar
            login_user(user, remember=True)

            flash('account created', category='success')

            # redirect url to home page
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)