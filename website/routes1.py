from crypt import methods
from flask import Blueprint

routes1 = Blueprint('routes1', __name__)

@routes1.route('/getAllPosts', methods=['GET'])
def getAllPosts():
    return "[1,2,3]"

@routes1.route('/createPost', methods=['POST'])
def createPost():
    return "post created"

@routes1.route('/getPosts', methods=['GET'])
def getPosts():
    return "own posts"