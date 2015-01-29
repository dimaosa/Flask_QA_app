from flask import Flask, render_template, redirect, url_for, request, session, flash

from flask.ext.sqlalchemy import SQLAlchemy 
from functools import wraps
import sqlite3

app = Flask(__name__)
#import different config for diffferent env
import os
app.config.from_object(os.environ['APP_SETTINGS'])

# create the sqlalchemy object
db = SQLAlchemy(app)

from models import *

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap


@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
	
	posts = []

	try:
		if request.method == 'POST':
			if request.form['title'] and request.form['post']:
				print request.form['title']
				print request.form['post']
			 	db.session.add(BlogPost(request.form['title'], request.form['post']))
			 	db.session.commit()

		posts = db.session.query(BlogPost).all()
	except:
		flash("Some error in db")
	return render_template("index.html", posts=posts)

@app.route('/welcome')
def welcome():
	return render_template("welcome.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid creantials. Please try again'
		else:
			session['logged_in'] = True
			flash('You were just logged in!')
			return redirect(url_for('home'))
	return render_template("login.html", error=error)
@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were just logged out!')
	return redirect(url_for('welcome'))


if __name__ == '__main__':
	app.run()


