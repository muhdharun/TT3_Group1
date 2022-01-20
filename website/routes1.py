from flask import Blueprint, Flask, Response, request, jsonify
from .models import User,Post,LikedPost,PostComment
from . import db
import json
import random

routes1 = Blueprint('routes1', __name__)

@routes1.route('/getAllPosts', methods=['GET'])
def getAllPosts():
    response = None
    try:

    #     data = {
    #     "Post_ID": 1,
    #     "Post_Title": "Relatable",
    #     "Post_Description": "Walking up and down the aisles for what seems like hours.",
    #     "Post_image": "https://preview.redd.it/jjvqtw9iapb81.gif?format=mp4&s=e333e78478df813b5b18ecd0905efc8b00ae210c"
    # }

        #data = db.Query(Post)
        posts = Post.query.all()
        data = []
        for post in posts:
            data.append({"Post_ID": post.id, "Post_Title": post.title, "Post_Description": post.description, "Post_Image": post.image, "User_Id": post.user_id})
        response = Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)

        response = Response(
            response=json.dumps({"message":"cannot get posts"}),
            status=500,
            mimetype="application/json"
        )

    return response

@routes1.route('/createPost', methods=['POST'])
def createPost():
    response = None
    try:
        postId = random.randint(1,1000000)
        #post = {"Post_ID": postId, "Post_Title": request.form["title"], "Post_Description": request.form["description"], "Post_Image": request.form["image"]}
        post = Post(
            id = postId,
            title = request.form.get("title"),
            description = request.form.get("description"),
            image = request.form.get("image"),
            user_id = request.form.get("userId"), #temporary
        )
        db.session.add(post)
        db.session.commit()

        response = Response(
            response=json.dumps({"message":"post created", "id":f'{postId}'}),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)

        response = Response(
            response=json.dumps({"message":"cannot create post"}),
            status=500,
            mimetype="application/json"
        )

    return response

#get logged in user's posts
@routes1.route('/getPosts/<userId>', methods=['GET'])
def getPosts(userId):
    response = None
    try:
        posts = Post.query.filter_by(user_id=userId)
        data = []
        for post in posts:
            data.append({"Post_ID": post.id, "Post_Title": post.title, "Post_Description": post.description, "Post_Image": post.image, "User_Id": post.user_id})
        response = Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )
    
    except Exception as ex:
        print(ex)

        response = Response(
            response=json.dumps({"message":"cannot get user's posts"}),
            status=500,
            mimetype="application/json"
        )

    return response

@routes1.route('/searchPost/<searchQuery>', methods=['GET'])
def searchPost(searchQuery):
    response = None
    try:
        search = "%{}%".format(searchQuery)
        posts = Post.query.filter(Post.title.like(search)).all()
        data = []
        for post in posts:
            data.append({"Post_ID": post.id, "Post_Title": post.title, "Post_Description": post.description, "Post_Image": post.image, "User_Id": post.user_id})
        
        posts = Post.query.filter(Post.description.like(search)).all()
        for post in posts:
            data.append({"Post_ID": post.id, "Post_Title": post.title, "Post_Description": post.description, "Post_Image": post.image, "User_Id": post.user_id})

        response = Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )
    
    except Exception as ex:
        print(ex)

        response = Response(
            response=json.dumps({"message":"cannot find posts"}),
            status=500,
            mimetype="application/json"
        )

    return response