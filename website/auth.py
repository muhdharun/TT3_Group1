from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully.', category='success')
                login_user(user, remember=True)
                return "Logged in"
                #return redirect(url_for('views.home'))
            else:
                flash('Incorrect password.', category='error')
                return "Incorrect password"
        else:
            flash('Email does not exist.', category='error')
            return "Email does not exist"
    return "Please log in"
    #return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password')
        password2 = request.form.get('password')
        birthday = request.form.get('birthday')
        phone = request.form.get('phone')
        city = request.form.get('city')
        country = request.form.get('country')
        age = request.form.get('age')
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Email is already in use.', category='error')
            return 'Email is already in use.'
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(name) < 1:
            flash('Please input a name.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email
                            , name=name
                            , password=generate_password_hash(password1, method='sha256')
                            , birthday=birthday
                            , phone=phone
                            , city=city
                            , country=country
                            , age=age)
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(email=email).first()
            login_user(user, remember=True)
            flash('Account created successfully.', category='success')
            return "Signed up succesfully"
            #return redirect(url_for('views.home'))
    return "Please sign up"
    #return render_template("signup.html", user=current_user)