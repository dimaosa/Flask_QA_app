from project import db
from project.models import BlogPost

# create the databaseand the db tables
db.create_all()


# insert
db.session.add(BlogPost("Good", "I\'m good", 1))
db.session.add(BlogPost("Well", "I\'m well", 1))
db.session.add(BlogPost("postgres", "we setup a local postgres", 1))

# commit the changes
db.session.commit()
