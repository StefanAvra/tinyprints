from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.forms import TinyForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', msg='this is home, where people vote')


@app.route('/new', methods=['GET', 'POST'])
def new():
    form = TinyForm()
    print('in /new', form.tiny_text.data, form.title.data)
    if form.validate_on_submit():
        print('after form validation')
        flash('tiny text submitted: {}, {}'.format(
            form.tiny_text.data, form.title.data))
        return redirect('/index')
    return render_template('new.html', msg='create a new one', form=form)


@app.route('/api')
def api():
    return 'this is where the api goes'

from app import models