## https://github.com/singingwolfboy/flask-dance-github/blob/main/github.py

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

FLASK_DEBUG = environ.get("FLASK_DEBUG")
FLASK_SECRET_KEY = environ.get("FLASK_SECRET_KEY")
GITHUB_OAUTH_CLIENT_ID = environ.get("GITHUB_OAUTH_CLIENT_ID")
GITHUB_OAUTH_CLIENT_SECRET = environ.get("GITHUB_OAUTH_CLIENT_SECRET")

## to allow http use
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

import os
from flask import Flask, redirect, url_for, session

from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
#app.secret_key = SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.config["SECRET_KEY"] = FLASK_SECRET_KEY
#app.config.update(
#    TESTING=True,
#    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
#)


app.config["GITHUB_OAUTH_CLIENT_ID"] = GITHUB_OAUTH_CLIENT_ID
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = GITHUB_OAUTH_CLIENT_SECRET
github_bp = make_github_blueprint()
app.register_blueprint(github_bp, url_prefix="/login")


@app.route("/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])

'''

from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
app.secret_key = "supersekrit"
blueprint = make_github_blueprint(
    client_id="my-key-here",
    client_secret="my-secret-here",
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])
'''

if __name__ == '__main__':
    app.run('0.0.0.0','5000')
