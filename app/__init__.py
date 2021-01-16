from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import models


@app.route('/')
def index():
    return render_template('index.html', msg='this is home, where people vote')


@app.route('/new')
def new():
    return render_template('new.html', msg='create a new one')


@app.route('/api')
def api():
    return 'this is where the api goes'
