from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    reviews = db.relationship('Review', backref='place', lazy=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0)
    filename = db.Column(db.String(300))  
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)\
