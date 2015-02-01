from project import app, db
from project.home.helper_classes import AnswerPost
from project.models import BlogPost, User, Answer, AnswerVote
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

def answerVoteAction(args):

	answer_id = int(args.split(',')[0])
	answer = Answer.query.filter_by(id=int(answer_id)).first()
	answerVote = AnswerVote.query.filter_by(
		user_id = current_user.id,
		answer_id = answer.id
		).first()

	#if Like present, then disLike and vise versa
	if bool(answerVote):
		answer.votes -= 1
		db.session.delete(answerVote)
	else:
		answer.votes += 1
		db.session.add(AnswerVote(
			answer_id, current_user.id)
		)
	db.session.commit()

################
#### routes ####
################



@home_blueprint.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):

	#retrieve data from form
	form = AddAnswer(request.form)

	#Post new Answer
	if form.validate_on_submit():
		newAnswer = Answer( form.body.data, current_user.id, post_id )
		db.session.add(newAnswer)
	#Like Answer
	elif request.method == 'POST':
		if request.form['action']:
			answerVoteAction(request.form['action'])
	#Increase number of views
	question = BlogPost.query.filter_by(id=int(post_id)).first()
	question.views +=1

	db.session.commit()
	
	answers = Answer.query.filter_by(blog_id=int(post_id)).order_by(Answer.id).all()
	answers = answers[::-1]

	#Create answerposts, by merging button state and answer
	answerposts = []
	current_user_id = int()
	if current_user.is_authenticated():
		current_user_id = current_user.id
	else:
		current_user_id = 0
	for answer in answers:
		answerposts.append(
			AnswerPost(
				answer,
				bool(AnswerVote.query.filter_by(
					user_id=current_user_id,
					answer_id = answer.id
					).first()
				)
			)
		)

	return render_template("post.html", post=question, form=form, 
		answerposts=answerposts)

@home_blueprint.route('/', methods=['GET', 'POST'])
def home():

	#retrieve form form
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
 	posts = [::-1]
	return render_template("index.html", form=form, posts=posts)

