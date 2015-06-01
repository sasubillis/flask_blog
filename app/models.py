from app import db
class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128))
  body = db.Column(db.Text)
    
  def __init__(self, title, body):
        self.title = title
        self.body = body


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))
	country = db.Column(db.String(64))

	def __init__(self, name, country):
		self.name = name
		self.country = country

