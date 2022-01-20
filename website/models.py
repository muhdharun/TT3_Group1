from . import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey

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
    liked_post = db.relationship('LikedPost')
    posts = db.relationship('Post')
    comments = db.relationship('PostComment')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(100000))
    image = db.Column(db.String()) #Not quite sure how database adds in an image
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    liked_post = db.relationship('LikedPost')
    comments = db.relationship('PostComment')
    
class LikedPost(db.Model):
    user_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True, autoincrement=False)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), primary_key=True, autoincrement=False)
    
class PostComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    comment = db.db.Column(db.String(1000))