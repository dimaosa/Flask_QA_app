from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired

class AddPost(Form):
    title = TextField('title', validators=[DataRequired()])
    post = TextAreaField('post', validators=[DataRequired()])

class AddAnswer(Form):
	body = TextAreaField('body', validators=[DataRequired()])