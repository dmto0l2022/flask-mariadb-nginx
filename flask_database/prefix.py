from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

GITHUB_OAUTH_CLIENT_ID = environ.get("GITHUB_OAUTH_CLIENT_ID")
GITHUB_OAUTH_CLIENT_SECRET = environ.get("GITHUB_OAUTH_CLIENT_SECRET")

app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('FLASK_SECRET_KEY')
blueprint = make_github_blueprint(
    client_id=GITHUB_OAUTH_CLIENT_ID,
    client_secret=GITHUB_OAUTH_CLIENT_SECRET,
)

app.register_blueprint(blueprint, url_prefix="/app/login")

@app.route("/app/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
