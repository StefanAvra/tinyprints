from flask import render_template, flash, redirect, session
from app import app, db

from app.forms import TinyForm
from app.models import TinyText
from random import randint


@app.route('/', methods=['GET', 'POST'])
def index():
    # form = VoteForm()
    # if form.validate_on_submit():
    #   pass
    t = TinyText.query.order_by(TinyText.id.desc()).all()
    return render_template('index.html', msg='this is home, where people vote', tiny_texts=t)


@app.route('/new', methods=['GET', 'POST'])
def new():
    form = TinyForm()
    if form.validate_on_submit():
        t = TinyText(text=form.tiny_text.data, title=form.title.data)
        db.session.add(t)
        db.session.commit()
        flash('tiny text submitted: {}, {}'.format(
            form.tiny_text.data, form.title.data))
        print(t.text)
        return render_template('index.html', highlight=t.id)

    msgs = [
        'send me a haiku',
        'can make ascii art?',
        'how do you feel today?',
        'shouldn\'t you be doing something else?',
        'i hope you\'re having a nice day',
        'any movie recommendations?',
        'what\'s on your mind lately?',
        'you\'re on your own on this one',
        'write something nice',
        'what should the world see?',
        'write a recipe',
        'write something that people will enjoy',
        'you got this',
        'don\'t spam'
    ]
    return render_template('new.html', msg=msgs[randint(0, len(msgs)-1)], form=form)


@app.route('/top')
def top():
    return render_template('top.html')


@app.route('/api')
def api():
    return 'this is where the api goes'
