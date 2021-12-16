from api_application import db
from datetime import datetime


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"{self.name}"