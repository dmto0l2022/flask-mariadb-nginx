from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import os

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

print(BASE_DIR)

GITHUB_OAUTH_CLIENT_ID = environ.get("GITHUB_OAUTH_CLIENT_ID")
GITHUB_OAUTH_CLIENT_SECRET = environ.get("GITHUB_OAUTH_CLIENT_SECRET")

print(GITHUB_OAUTH_CLIENT_ID)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"]="1"

class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]

app = Flask(__name__)

#app.wsgi_app = PrefixMiddleware(app.wsgi_app)##, prefix='/app')                    

#FLASK_SECRET_KEY_VAR = environ.get('FLASK_SECRET_KEY')

#print(FLASK_SECRET_KEY_VAR)

#app.config['SECRET_KEY'] = FLASK_SECRET_KEY_VAR

##app.secret_key = FLASK_SECRET_KEY_VAR

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['SESSION_TYPE'] = 'filesystem'

blueprint = make_github_blueprint(
    client_id=GITHUB_OAUTH_CLIENT_ID,
    client_secret=GITHUB_OAUTH_CLIENT_SECRET,
)

app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/app/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
