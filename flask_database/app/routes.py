from flask import render_template
from app import app

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/index')
def index():
    user = {'username': 'Andy'}
    return render_template('index.html', title='Index', user=user)

@app.route('/user')
def user():
    user = {'username': 'Andy'}
    return render_template('user.html', title='Basic', user=user)
