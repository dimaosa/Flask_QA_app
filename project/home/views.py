from project import app, db
from project.models import BlogPost, User
from flask import flash, redirect, session, url_for, render_template, request, Blueprint

from project.users.form import AddPost
################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

### routes ###
@home_blueprint.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
	post = BlogPost.query.filter_by(id=int(post_id)).first()

	try:
		user = User.query.filter_by(id=int(post.author_id)).first()
	except:
		user = User(' ',' ',' ')

	return render_template("post.html", post=post, user=user)

@home_blueprint.route('/', methods=['GET', 'POST'])
def home():

	form = AddPost(request.form)
	
	try:
		if request.method == 'POST':
			flash("I am in POST")
			if request.form['title'] and request.form['post']:
				flash(request.form['title'])
				flash(request.form['post'])
			 	db.session.add(BlogPost(request.form['title'], request.form['post']))
			 	db.session.commit()
			else:
				flash("Enter both title and post")
	except:
		flash("Some error in db")

 	posts = db.session.query(BlogPost).all()
 	posts = reversed(posts)
	return render_template("index.html", form=form, posts=posts)

@home_blueprint.route('/welcome')
def welcome():
	return render_template("welcome.html")
