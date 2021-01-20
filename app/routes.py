from functools import wraps
from flask import render_template, flash, redirect, session, url_for, request
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash

from app.forms import TinyForm, VoteForm
from app.models import TinyText
import random


WORDS  = []

with app.open_resource('words.txt', 'rt') as f:
    WORDS = f.read().splitlines()    


@app.before_request
def init_session():
    session.setdefault('voted', [])
    session.permanent = True
    print(session)


@app.route('/', methods=['GET', 'POST'])
@app.route('/new', methods=['GET', 'POST'])
@app.route('/hot', methods=['GET', 'POST'])
def index():
    upvote_form = VoteForm()
    if upvote_form.validate_on_submit():
        t = TinyText.query.get(upvote_form.tiny_text_id.data)
        if t and not t.voting_closed:
            if t.id not in session.get('voted'):
                t.up()
                db.session.add(t)
                db.session.commit()
                voted_list = session.pop('voted')
                voted_list.append(t.id)
                session['voted'] = voted_list
                print(f'upvote for {t}')
                print(session['voted'])
            else:
                print(f'session already voted for {t.id}')
        return redirect(url_for('index'))
    
    rule = request.url_rule
    if 'hot' in rule.rule:
        t_list = TinyText.query.order_by(TinyText.votes.desc()).filter_by(voting_closed=False).all()
    else:
        t_list = TinyText.query.order_by(TinyText.id.desc()).filter_by(voting_closed=False).all()
    return render_template('index.html', tiny_texts=t_list, upvote_form=upvote_form, past_upvotes=session.get('voted'))

@app.route('/t/')
@app.route('/t/<id>', methods=['GET', 'POST'])
def view_single(id=None):
    t = TinyText.query.get(id)
    print(t)
    upvote_form = VoteForm()
    if upvote_form.validate_on_submit():
        t = TinyText.query.get(upvote_form.tiny_text_id.data)
        if t and not t.voting_closed:
            if t.id not in session.get('voted'):
                t.up()
                db.session.add(t)
                db.session.commit()
                voted_list = session.pop('voted')
                voted_list.append(t.id)
                session['voted'] = voted_list
                print(f'upvote for {t}')
                print(session['voted'])
            else:
                print(f'session already voted for {t.id}')
        return redirect(url_for('view_single', id=t.id))

    if t:
        return render_template('single.html', tiny_text=t, upvote_form=upvote_form, past_upvotes=session.get('voted'))
    else:
        return redirect('/')


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = TinyForm()
    if form.is_submitted():
        if form.validate():
            t = TinyText(text=ascii(form.tiny_text.data), title=ascii(form.title.data))
            tiny_pw = f'{random.choice(WORDS)}#{random.randint(0, 999)}'
            t.pw_hash = generate_password_hash(tiny_pw)
            db.session.add(t)
            db.session.commit()
            flash('this is your tiny password:')
            flash(tiny_pw, category='pw')
            flash('you can use it to delete the post')
            print(t.text)
            return redirect(url_for('view_single', id=t.id))
        else:
            flash('no.')
    msgs = [
        'send me a haiku',
        'can you make ascii art?',
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
        'don\'t spam',
        'what is something nobody knows?'
    ]
    return render_template('create.html', msg=random.choice(msgs), form=form)


@app.route('/top')
def top():
    return redirect(url_for('index'))


@app.route('/api')
def api():
    return 'this is where the api goes'
