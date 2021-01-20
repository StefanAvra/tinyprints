from app import db
from datetime import datetime


class TinyText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32*24))
    title = db.Column(db.String(32))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    votes = db.Column(db.Integer, default=0, index=True)
    voting_closed = db.Column(db.Boolean, default=False)
    voting_closed_timestamp = db.Column(db.DateTime, index=True)
    pw_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<TinyText id:{}, created:{}, title:{}, votes:{}>'.format(self.id, self.created, self.title, self.votes)

    def up(self):
        if not self.voting_closed:
            self.votes += 1

    def close(self):
        self.voting_closed = True
        self.voting_closed_timestamp = datetime.utcnow()
    