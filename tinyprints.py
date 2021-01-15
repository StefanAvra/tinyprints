from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', msg='this is home, where people vote')

@app.route('/new')
def new():
    return render_template('new.html' ,msg='create a new one')