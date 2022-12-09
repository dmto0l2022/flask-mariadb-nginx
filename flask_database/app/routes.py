#from flask import render_template
from flask import render_template, flash, redirect, url_for

from flask import Flask, render_template_string

##from app import app
from flask import current_app as app

from flask_security import Security, SQLAlchemyUserDatastore, auth_required, hash_password
from flask_security.models import fsqla_v3 as fsqla

##>> from flask_dance.contrib.github import make_github_blueprint, github

##login = app.login_manager
#from app import db
db = app.extensions['sqlalchemy'].db

from flask_login import current_user

##from flask_login import login_required

from app.models import User

##from app.forms import LoginForm

##from app.forms import RegistrationForm

# Views
@app.route("/app/check/")
@auth_required()
def check():
    return render_template_string("Hello {{ current_user.email }}")

@app.route('/app/')
def hello():
    return "Hello, World!"

@app.route('/app/welcome/')
def welcome():
    return render_template('welcome.html')

##>> @app.route("/app/login")
##>> def gitlogin():
##>>     if not github.authorized:
##>>         return redirect(url_for("github.login"))
##>>     resp = github.get("/user")
##>>     assert resp.ok
##>>     return "You are @{login} on GitHub".format(login=resp.json()["login"])

@app.route('/app/index')
##@login_required
def index():
    user = {'username': 'Andy'}
    ##>> if not github.authorized:
    ##>>     return redirect(url_for("github.login"))
    ##>> resp = github.get("/user")
    ##>> assert resp.ok
    return render_template('index.html', title='Index', user=user)

@app.route('/app/test')
def test():
    return render_template('test.html', title='Index')

@app.route('/app/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/app/user')
def user():
    user = {'username': 'Andy'}
    return render_template('user.html', title='Basic', user=user)

'''
@app.route('/app/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        ##>> return redirect(url_for('gitlogin'))
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)
'''
'''
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
'''
'''
@app.route('/app/login', methods=['GET', 'POST'])
def locallogin():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
'''

'''
@app.route('/app/login', methods=['GET', 'POST'])
def userlogin():
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
    return render_template('userlogin.html', title='Sign In', form=form)
'''

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
'''
@app.route('/app/logout')
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for('index'))
'''
