from project import db
from project.models import BlogPost

# create the databaseand the db tables
db.create_all()


# insert
for i in xrange(10):
	message = "This is {} post".format(i)
	db.session.add(BlogPost(message, "and I\'m good", 8))

# commit the changes
db.session.commit()
