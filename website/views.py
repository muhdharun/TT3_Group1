from flask import Blueprint, render_template, request, flash, redirect, url_for
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
        return redirect(url_for("views.home"))
    except:
        flash('Problem occurred while deleting post, try again or contact support.', category='error')
        return redirect(url_for("views.home"))
    
@views.route('/updatePost/<int:id>', methods=['GET','POST'])
def updatePost(id):
    post_to_update = Post.query.get_or_404(id)
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']
        
        if (title != None) and (len(title) != 0):
            post_to_update.title = title
        
        post_to_update.description = description
        post_to_update.image = image
        
        try:
            db.session.commit()
            return redirect(url_for("views.home"))
        
        except:
            flash('Problem occurred while editing post, try again or contact support.', category='error')
            return redirect(url_for("views.home"))
            
    else:
        return render_template("update.html", user=current_user)