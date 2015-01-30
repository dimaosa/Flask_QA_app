from project import app, db
from project.models import BlogPost, User
from flask import flash, redirect, session, url_for, render_template, request, Blueprint
from flask.ext.login import current_user

from form import AddPost, AddAnswer
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

	form = AddAnswer(request.form)
	if form.validate_on_submit():
		flash( form.body.data )

	post = BlogPost.query.filter_by(id=int(post_id)).first()

	return render_template("post.html", post=post, form=form)

@home_blueprint.route('/', methods=['GET', 'POST'])
def home():

	form = AddPost(request.form)
	try:
		if form.validate_on_submit():
			newQuestion = BlogPost(
				form.title.data,
				form.post.data,
				current_user.id
			)
			db.session.add(newQuestion)
			db.session.commit()
			flash("New Question was added")
	except:
		flash("Some error in db")

 	posts = db.session.query(BlogPost).all()
 	posts = reversed(posts)
	return render_template("index.html", form=form, posts=posts)

@home_blueprint.route('/welcome')
def welcome():
	return render_template("welcome.html")
