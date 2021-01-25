from app.models import Deadline, TinyText
from app import db
from flask import session
from datetime import datetime, timedelta


def init_deadline():
    """Creates deadline if there is none"""
    deadline = Deadline.query.first()
    if not deadline:
        deadline = Deadline(deadline=datetime.utcnow() + timedelta(1))
        db.session.add(deadline)
        db.session.commit()


def renew_deadline(new_deadline=None):
    """Sets new deadline, default is now + 24hrs"""
    deadline = Deadline.query.first()
    if not deadline:
        deadline = Deadline()
    if new_deadline:
        deadline.deadline = new_deadline
    else:
        deadline.deadline = datetime.utcnow() + timedelta(1)
    db.session.add(deadline)
    db.session.commit()


def deadline_reached():
    """Closes voting for highest in 'hot' and calls renew_deadline()"""
    t = TinyText.query.order_by(TinyText.votes.desc()).filter_by(voting_closed=False).first()
    t.close()
    db.session.add(t)
    renew_deadline()


