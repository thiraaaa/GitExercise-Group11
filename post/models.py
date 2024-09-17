from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class post(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title - db.column(db dtring(100), nullable=False)
    