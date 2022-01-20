from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    from .routes1 import routes1
    from .views import views
    #from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    #app.register_blueprint(auth, url_prefix='/')


    app.register_blueprint(routes1, url_prefix='/')

    return app