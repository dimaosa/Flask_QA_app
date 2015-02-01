from project import db, bcrypt

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class BlogPost(db.Model):

	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	description = db.Column(db.String, nullable=False)
	author_id = db.Column(db.Integer, ForeignKey('users.id'))
	answer = db.relationship("Answer",  backref="blogpost")
	pub_date = db.Column(db.DateTime)
	views = db.Column(db.Integer)

	def __init__(self, title, description, author_id, pub_date=None):
		self.title = title
		self.description = description
		if pub_date is None:
			pub_date = datetime.now()
		self.pub_date = pub_date
		self.author_id = author_id
		self.views = 0

	def __repr__(self):
		return '{} - {}'.format(self.title, self.description).uncode('utf-8')
class Answer(db.Model):

	__tablename__ = "answers"

	id = db.Column(db.Integer, primary_key=True)
	answer = db.Column(db.String, nullable=False)
	pub_date = db.Column(db.DateTime)
	votes = db.Column(db.Integer)
	user_id = db.Column(db.Integer, ForeignKey('users.id'))
	blog_id = db.Column(db.Integer, ForeignKey('posts.id'))
	answervote = db.relationship("AnswerVote", backref="answer")
	
	def __init__(self, answer, user_id, blog_id, pub_date=None):

		self.answer = answer
		if pub_date is None:
			pub_date = datetime.now()
		self.pub_date = pub_date
		self.user_id = user_id
		self.blog_id = blog_id
		self.votes = 0

	def __repr__(self):
		return '<Answer - {}, Author - {}>'.format(self.answer, self.author)
class User(db.Model):

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	post = db.relationship("BlogPost",  backref="author")
	answer = db.relationship("Answer",  backref="author")
	answervote = db.relationship("AnswerVote", backref="author")

	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = bcrypt.generate_password_hash(password)
	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '{} - {}'.format(self.name, self.email)

class AnswerVote(db.Model):
	__tablename__ = "answervotes"

	id = db.Column(db.Integer, primary_key=True)
	answer_id = db.Column(db.Integer, ForeignKey('answers.id'))
	user_id = db.Column(db.Integer, ForeignKey('users.id'))

	def __init__(self, answer_id, user_id):
		self.answer_id = answer_id;
		self.user_id = user_id;
