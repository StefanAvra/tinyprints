from app import db
from datetime import datetime


class TinyText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32*24))
    title = db.Column(db.String(32))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    votes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<TinyText id:{}, created:{}, title:{}, votes:{}>'.format(self.id, self.created, self.title, self.votes)    
