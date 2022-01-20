from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Post

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "hello world"

@views.route('/deletePost/<int:id>')
def deletePost(id):
    post_to_delete = Post.query.get_or_404(id)
    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash('Post deleted successfully.', category='success')
        return render_template("home.html", user=current_user)
    except:
        flash('Problem occurred while deleting post, try again or contact support.', category='error')
        return render_template("home.html", user=current_user)