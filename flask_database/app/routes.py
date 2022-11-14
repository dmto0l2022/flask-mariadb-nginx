#from flask import render_template
from flask import render_template, flash, redirect, url_for
##from app import app
from flask import current_app as app

from flask_login import current_user, login_user, logout_user

from flask_login import login_required

from app.models import User

from app.forms import LoginForm

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/index')
@login_required
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

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    form = LoginForm()
#    if form.validate_on_submit():
#        flash('Login requested for user {}, remember_me={}'.format(
#            form.username.data, form.remember_me.data))
#        return redirect(url_for('index'))
#    return render_template('login.html', title='Sign In', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

'''
def login():
    # ...
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
'''

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
