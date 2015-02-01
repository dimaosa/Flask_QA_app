from project import db
from project.models import BlogPost
import random
# create the databaseand the db tables
db.create_all()

answers = [
	"Which is heavier a ton of gold or a ton of silver?",
	"Is it legal for a man to marry his widow's sister?",
	"Why is it against the law for a person living in New York to be buried in California?",
	"Which month has 28 days?",
	"How many times can you subtract 10 from 100?",
	"Before Mt. Everest was discovered, which was the highest mountain in the world?",
	"If an electric train is traveling south, which way is the smoke going?"
]
# insert
for answer in answers:
	message = answer
	db.session.add(BlogPost(message, "maybe you know", random.randint(2, 6)))

# commit the changes
db.session.commit()
