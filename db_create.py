from project import db
from project.models import BlogPost

# create the databaseand the db tables
db.create_all()


# insert
for i in xrange(10):
	message = "Is this a {} question?".format(i)
	db.session.add(BlogPost(message, "maybe you know", 4))

# commit the changes
db.session.commit()
