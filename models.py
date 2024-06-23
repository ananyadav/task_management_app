# models.py
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.Date)

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'
