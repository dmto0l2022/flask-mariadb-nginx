#from flask import render_template
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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

#@app.route('/login')
#def login():
#    form = LoginForm()
#    return render_template('login.html', title='Sign In', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

