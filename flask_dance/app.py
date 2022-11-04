## https://github.com/singingwolfboy/flask-dance-github/blob/main/github.py

'''
import os
from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
app.config["GITHUB_OAUTH_CLIENT_ID"] = os.environ.get("GITHUB_OAUTH_CLIENT_ID")
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = os.environ.get("GITHUB_OAUTH_CLIENT_SECRET")
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

if __name__ == '__main__':
    app.run('0.0.0.0','5000')
