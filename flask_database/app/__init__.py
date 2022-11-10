from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#from config import Config

import os

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

app = Flask(__name__)
print('key from file: ')
print(environ.get('FLASK_SECRET_KEY'))

app.config['SECRET_KEY'] = environ.get('FLASK_SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
