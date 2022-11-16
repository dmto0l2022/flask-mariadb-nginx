import os

from os import environ, path

from dotenv import load_dotenv

from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)



BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

print(BASE_DIR)

GITHUB_OAUTH_CLIENT_ID = environ.get("GITHUB_OAUTH_CLIENT_ID")
GITHUB_OAUTH_CLIENT_SECRET = environ.get("GITHUB_OAUTH_CLIENT_SECRET")

print("client:" ,GITHUB_OAUTH_CLIENT_ID)
print("secret:" ,GITHUB_OAUTH_CLIENT_SECRET)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"]="1"

app.secret_key = 'myscretkey'
#configuraciones de oauth
oauth = OAuth(app)
github = oauth.register(
    name='github',
    client_id=GITHUB_OAUTH_CLIENT_ID,
    client_secret=GITHUB_OAUTH_CLIENT_SECRET,
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

@app.route("/")
def index():
    return f'Hello!'
  
@app.route('/login')
def registro():
   github = oauth.create_client('github')
   redirect_uri = url_for('authorize', _external=True)
   return github.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
   github = oauth.create_client('github')
   token = github.authorize_access_token()
   resp = github.get('user', token=token)
   profile = resp.json()
   # do something with the token and profile
   print(profile, token)
   return redirect('/')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port='5000')
