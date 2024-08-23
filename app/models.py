from app import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.Text, nullable=True)
    persons = db.Column(db.String(200))
    places = db.Column(db.String(200))
    topic = db.Column(db.String(100))
    tragedy_level = db.Column(db.Integer)
    humor_level = db.Column(db.Integer)
    political_relevance = db.Column(db.Integer)
