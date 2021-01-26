"""This is the minimum auth I could come up with. Users don't need to authenticate for now, so that's ok"""
from app import app
from werkzeug.security import generate_password_hash, check_password_hash

AUTH_HASH = generate_password_hash(app.config['AUTH_SECRET'])

def check_auth(pw):
    return check_password_hash(AUTH_HASH, pw)