##https://archbird.io/article/how-to-combine-one-or-more-dash-apps-with-existing-wsgi-apps/

from flask import Flask

flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return 'Hello Flask app'
  
  
