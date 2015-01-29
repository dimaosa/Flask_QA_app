from flask import Flask, flash, redirect, session, url_for, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy 
from functools import wraps
import os

### config ###
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint


app.register_blueprint(users_blueprint)


### helper function ###
def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('users.login'))
	return wrap

### routes ###

@app.route('/', methods=['GET', 'POST'])
@login_required
def home():

	try:
		if request.method == 'POST':
			flash("I am in POST")
			if request.form['title'] and request.form['post']:
				flash(request.form['title'])
				flash(request.form['post'])
			 	db.session.add(BlogPost(request.form['title'], request.form['post']))
			 	db.session.commit()
	except:
		flash("Some error in db")

 	posts = db.session.query(BlogPost).all()
	return render_template("index.html", posts=posts)

@app.route('/welcome')
def welcome():
	return render_template("welcome.html")

### run server ###
if __name__ == '__main__':
	app.run()
