from app.models import Deadline, TinyText
from app import db
from flask import session
from datetime import datetime, timedelta


def renew_deadline(new_deadline=None):
    """Creates new deadline, default is now + 24hrs"""
    deadline = Deadline.query.first()
    if not deadline:
        deadline = Deadline()
    if new_deadline:
        deadline.deadline = new_deadline
    else:
        deadline.deadline = datetime.utcnow() + timedelta(1)
    db.session.add(deadline)
    db.session.commit()
