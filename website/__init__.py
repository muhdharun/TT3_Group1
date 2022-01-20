from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from werkzeug.security import generate_password_hash
from flask_login import LoginManager
from flask_cors import CORS, cross_origin

db = SQLAlchemy()
DB_NAME = "database.db"
"""example users to add"""
users_to_add = [{
    "User_ID": 1,
    "Name": "Brose McCreery",
    "Age": 22,
    "Birthday": "1993-03-01",
    "Email": "bmccreery0@bloomberg.com",
    "Phone": "(858) 1604103",
    "City": "Gujba",
    "Country": "Nigeria",
  },
  {
    "User_ID": 2,
    "Name": "Darla Joret",
    "Age": 23,
    "Birthday": "1996-09-08",
    "Email": "djoret1@latimes.com",
    "Phone": "(859) 9667080",
    "City": "Zoumaping",
    "Country": "China",
  }]

def create_app():
    app = Flask(__name__)
    CORS(app, resources={ r'/*': {'origins': 'http://localhost:8000'}})
    app.config['SECRET_KEY'] = '123'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #from .routes1 import routes1
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    #app.register_blueprint(routes1, url_prefix='/')

    from .models import User,Post,LikedPost,PostComment
    
    login_manager= LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    create_database(app)
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database')