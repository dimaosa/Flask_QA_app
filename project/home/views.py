from project import app, db
from project.models import BlogPost, User, Answer
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

def answerVotesCounter(answer_id, state):

	answer = Answer.query.filter_by(id=int(answer_id)).first()
	if state:
		answer.votes += 1
	else:
		answer.votes -= 1
	db.session.commit()
################
#### routes ####
################



@home_blueprint.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):


	form = AddAnswer(request.form)

	if form.validate_on_submit():
		newAnswer = Answer(
			form.body.data,
			current_user.id,
			post_id
			)
		db.session.add(newAnswer)

	if request.method == 'POST':
		print "in POST"

	post = BlogPost.query.filter_by(id=int(post_id)).first()
	post.views +=1
	db.session.commit()
	answers = Answer.query.filter_by(blog_id=int(post_id)).all()
	answers = reversed(answers)

	return render_template("post.html", post=post, form=form, answers=answers)

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

 	posts = db.session.query(BlogPost).order_by(BlogPost.id).all()
 	posts = reversed(posts)
 	flash(posts)
	return render_template("index.html", form=form, posts=posts)

