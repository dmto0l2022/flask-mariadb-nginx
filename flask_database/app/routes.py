#from flask import render_template
from flask import render_template, flash, redirect, url_for
##from app import app
from flask import current_app as app

from flask_dance.contrib.github import make_github_blueprint, github

login = app.login_manager
#from app import db
db = app.extensions['sqlalchemy'].db

from flask_login import current_user, login_user, logout_user

from flask_login import login_required

from app.models import User

from app.forms import LoginForm

from app.forms import RegistrationForm

@app.route('/app/')
def hello():
    return "Hello, World!"

@app.route("/app/login")
def gitlogin():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])

@app.route('/app/index')
@login_required
def index():
    user = {'username': 'Andy'}
    return render_template('index.html', title='Index', user=user)

@app.route('/app/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/app/user')
def user():
    user = {'username': 'Andy'}
    return render_template('user.html', title='Basic', user=user)

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
        return redirect(url_for('gitlogin'))
    return render_template('register.html', title='Register', form=form)

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

'''
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

@app.route('/app/logout')
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for('index'))
