from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/user')
def user():
    user = {'username': 'Andy'}
    return render_template('user.html', title='Basic', user=user)
