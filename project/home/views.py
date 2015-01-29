from project import app, db
from project.models import BlogPost
from flask import flash, redirect, session, url_for, render_template, request, Blueprint

################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

### routes ###

@home_blueprint.route('/', methods=['GET', 'POST'])
def home():

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
	return render_template("index.html", posts=posts)

@home_blueprint.route('/welcome')
def welcome():
	return render_template("welcome.html")
