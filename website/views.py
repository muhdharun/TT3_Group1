from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from flask_login import login_required, current_user
from . import db
from .models import Post
import json
import random

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    response = None
    try:
        
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

@views.route('/deletePost/<int:id>', methods=['GET','DELETE'])
def deletePost(id):
    post_to_delete = Post.query.get_or_404(id)
    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash('Post deleted successfully.', category='success')
        return "deleted post"
        #return redirect(url_for("views.home"))
    except:
        flash('Problem occurred while deleting post, try again or contact support.', category='error')
        return "Failed to delete"
        #return redirect(url_for("views.home"))
    
@views.route('/updatePost/<int:id>', methods=['GET','PATCH'])
def updatePost(id):
    post_to_update = Post.query.get_or_404(id)
    if request.method == 'PATCH':
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']
        
        if (title != None) and (len(title) != 0):
            post_to_update.title = title
        
        post_to_update.description = description
        post_to_update.image = image
        
        try:
            db.session.commit()
            return "successfilly updated"
            #return redirect(url_for("views.home"))
        
        except:
            flash('Problem occurred while editing post, try again or contact support.', category='error')
            return "Failed to update"
            #return redirect(url_for("views.home"))
            
    else:
        return "Welcome to update"
        #return render_template("update.html", user=current_user)

@views.route('/getAllPosts', methods=['GET'])
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

@views.route('/createPost', methods=['POST'])
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
@views.route('/getPosts/<userId>', methods=['GET'])
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

@views.route('/searchPost/<searchQuery>', methods=['GET'])
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