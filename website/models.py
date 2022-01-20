from . import db
from flask_login import UserMixin
from sqlalchmey import ForeignKey

user_post_table = db.Table('user_project_table',
                              db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                              db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
)


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
    liked_posts = db.relationship('LikedPost')
    posts = db.relationship('Post')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(150), nullable=False)
    post_title = db.Column(db.String(100000))
    post_image = db.Column(db.String()) #Not quite sure how database adds in an image
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    liked_posts = db.relationship('LikedPost')
    
class LikedPost(db.Model):
    user_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True, autoincrement=False)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), primary_key=True, autoincrement=False)