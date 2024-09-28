from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    photos = db.relationship('Photo', backref='place', lazy=True)

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=True)  
    review = db.Column(db.Text, nullable=True)
    likes = db.Column(db.Integer, default=0)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)


