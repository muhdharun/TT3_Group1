from . import db
from flask_login import UserMixin

#Added in password
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(50))
    name = db.Column(db.String(50))
    birthday = db.Column(db.DateTime(timezone=False), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)