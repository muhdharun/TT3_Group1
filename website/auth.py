from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, Response
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import json
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
                logged_in_user = {"User_Id": user.id
                             , "Name": user.name
                             , "Email": user.email
                             , "Birthday": user.birthday
                             , "City": user.city
                             , "Country": user.country
                             , "Age": user.age
                             , "Liked_Post": user.liked_post
                             , "Posts": user.posts
                             , "Comments": user.comments}
                response = Response(response=json.dumps(logged_in_user),
                                    status=200,
                                    mimetype="application/json"
                                    )
                login_user(user, remember=True)
                #return redirect(url_for('views.home'))
                return response
            else:
                flash('Incorrect password.', category='error')
                response = Response(response=json.dumps({"message":"Incorrect password."})
                                    , status=500
                                    , mimetype="application/json")
                #return "Incorrect password"
                return response
        else:
            flash('Email does not exist.', category='error')
            response = Response(response=json.dumps({"message":"Email does not exist."})
                                , status=500
                                , mimetype="application/json")
            return response
            #return "Email does not exist"
    
    response = Response(response=json.dumps({"message":"Please log in"})
                        , status=500
                        , mimetype="application/json")
    return response
    #return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    response = Response(response=json.dumps({"message":"Logged out."})
                        , status=200
                        , mimetype="application/json")
    return response
    #return redirect(url_for('auth.login'))

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
            logged_in_user = {"User_Id": user.id
                             , "Name": user.name
                             , "Email": user.email
                             , "Birthday": user.birthday
                             , "City": user.city
                             , "Country": user.country
                             , "Age": user.age
                             , "Liked_Post": user.liked_post
                             , "Posts": user.posts
                             , "Comments": user.comments}
            response = Response(response=json.dumps(logged_in_user),
                                status=200,
                                mimetype="application/json"
                                )
            login_user(user, remember=True)
            flash('Account created successfully.', category='success')
            #return "Signed up succesfully"
            return response
            #return redirect(url_for('views.home'))
    response = Response(response=json.dumps({"message":"Please sign up"})
                        , status=500
                        , mimetype="application/json")
    return response
    #return "Please sign up"
    #return render_template("signup.html", user=current_user)