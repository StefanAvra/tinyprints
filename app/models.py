from app import db
from datetime import datetime

class TinyText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32*24))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
