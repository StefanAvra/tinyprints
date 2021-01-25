from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


def renew_deadline(new_deadline=None):
    """Creates new deadline, default is now + 24hrs"""
    deadline = Deadline.query.first()
    if new_deadline:
        deadline.deadline = new_deadline
    else:
        deadline.deadline = datetime.utcnow() + timedelta(1)
    db.session.add(deadline)
    db.session.commit()

