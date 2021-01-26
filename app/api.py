from flask import jsonify
from app.models import TinyText, Deadline
from app import deadline_mgmt, auth


def get_last_winner():
    winner = TinyText.query.order_by(TinyText.voting_closed_timestamp.desc()).filter_by(voting_closed=True).first()
    return jsonify(winner.to_dict())

def close_voting(pw):
    if not auth.check_auth(pw):
        return 'not ok', 401
    deadline_mgmt.deadline_reached()
    return 'ok'
