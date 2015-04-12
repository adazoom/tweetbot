from flask.ext.sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Tweets(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tweetID = db.Column(db.Integer) 
	tweetText = db.Column(db.Text)

	def __init__(self, tweetID, tweetText):
		self.tweetID = tweetID 
		self.tweetText = tweetText 
		
