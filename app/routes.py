from functools import wraps
from flask import render_template, flash, redirect, session, url_for, request, jsonify
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash

from app.forms import TinyForm, VoteForm, DeleteForm
from app.models import TinyText, Deadline
import random
import secrets
import string
from datetime import datetime, timedelta


@app.before_request
def init_session():
    session.setdefault('voted', [])
    session.permanent = True
    print(session)


@app.route('/', methods=['GET', 'POST'])
@app.route('/new', methods=['GET', 'POST'])
def index():
    site_data = init_site_data()
    page = request.args.get('p', 1, type=int)
    site_data['curr_page'] = page
    upvote_form = VoteForm()
    if upvote_form.validate_on_submit():
        handle_upvote(upvote_form, 'index')
    
    if '/' == request.url_rule.rule:
        site_data['title'] = 'home'
    else:
        site_data['title'] = 'new'
    t_list = TinyText.query.order_by(TinyText.id.desc()).filter_by(voting_closed=False).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    site_data['next_page'] = url_for('index', p=t_list.next_num) if t_list.has_next else None
    site_data['prev_page'] = url_for('index', p=t_list.prev_num) if t_list.has_prev else None

    return render_template('index.html', tiny_texts=t_list.items, upvote_form=upvote_form, past_upvotes=session.get('voted'), site_data=site_data)


@app.route('/hot', methods=['GET', 'POST'])
def hot():
    site_data = init_site_data()
    site_data['title'] = 'hottest prints'
    site_data['deadline'] = Deadline.query.first().deadline
    page = request.args.get('p', 1, type=int)
    site_data['curr_page'] = page
    upvote_form = VoteForm()
    if upvote_form.validate_on_submit():
        handle_upvote(upvote_form, 'hot')
    t_list = TinyText.query.order_by(TinyText.votes.desc()).filter_by(voting_closed=False).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    site_data['next_page'] = url_for('hot', p=t_list.next_num) if t_list.has_next else None
    site_data['prev_page'] = url_for('hot', p=t_list.prev_num) if t_list.has_prev else None
    return render_template('index.html', tiny_texts=t_list.items, upvote_form=upvote_form, past_upvotes=session.get('voted'), site_data=site_data)


@app.route('/top')
def top():
    site_data = init_site_data()
    page = request.args.get('p', 1, type=int)
    site_data['curr_page'] = page
    t_list = TinyText.query.order_by(TinyText.votes.desc()).filter_by(voting_closed=True).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    site_data['next_page'] = url_for('top', p=t_list.next_num) if t_list.has_next else None
    site_data['prev_page'] = url_for('top', p=t_list.prev_num) if t_list.has_prev else None
    return render_template('index.html', tiny_texts=t_list.items, site_data=site_data)


@app.route('/t/')
@app.route('/t/<id>', methods=['GET', 'POST'])
def view_single(id=None):
    t = TinyText.query.get(id)
    upvote_form = VoteForm()
    if upvote_form.validate_on_submit():
        handle_upvote(upvote_form, 'view_single', id)

    if t:
        delete_form = DeleteForm()
        if delete_form.validate_on_submit():
            t = TinyText.query.get(delete_form.delete_id.data)
            if t and t.pw_hash and check_password_hash(t.pw_hash, delete_form.delete_pw.data):
                db.session.delete(t)
                db.session.commit()
                flash('your post was deleted')
                return redirect('/')
        return render_template('single.html', tiny_text=t, upvote_form=upvote_form, past_upvotes=session.get('voted'), delete_form=delete_form)
    else:
        return redirect('/')


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = TinyForm()
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
    site_data = init_site_data()
    site_data['title'] = 'create a tiny print'
    if form.is_submitted():
        if form.validate():
            t = TinyText(text=form.tiny_text.data, title=form.title.data)
            abc = string.ascii_letters + string.digits
            tiny_pw = ''.join(secrets.choice(abc) for i in range(10))
            t.pw_hash = generate_password_hash(tiny_pw)
            db.session.add(t)
            db.session.commit()
            flash('this is your tiny password:')
            flash(tiny_pw, category='pw')
            flash('you can use it to delete the post')
            return redirect(url_for('view_single', id=t.id))
        else:
            flash('no.')
            return redirect(url_for('create'))
    return render_template('create.html', msg=random.choice(msgs), form=form, site_data=site_data)



@app.route('/api')
def api_index():
    request.args.get('', 1, type=int)
    return 'hmmm'

@app.route('/api/winner')
def api_get_winner():
    winner = TinyText.query.order_by(TinyText.voting_closed_timestamp.desc()).filter_by(voting_closed=True).first()
    return jsonify(winner.to_dict())


def init_site_data():
    site_data = {
        'title': '',
        'msg': '',
        'next_page': None,
        'prev_page': None,
        'curr_page': None
    }
    return site_data


def handle_upvote(upvote_form, redirect_to='index', redirect_id=None):
    t = TinyText.query.get(upvote_form.tiny_text_id.data)
    if t and not t.voting_closed:
        if t.id not in session.get('voted'):
            t.up()
            db.session.add(t)
            db.session.commit()
            voted_list = session.pop('voted')
            voted_list.append(t.id)
            session['voted'] = voted_list
        else:
            print(f'session already voted for {t.id}')
    return redirect(url_for(redirect_to, p=redirect_id))

