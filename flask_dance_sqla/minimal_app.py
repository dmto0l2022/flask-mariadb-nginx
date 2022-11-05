##

import os
from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

####  https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

#FLASK_DEBUG = environ.get("FLASK_DEBUG")
#FLASK_SECRET_KEY = environ.get("FLASK_SECRET_KEY")
#GITHUB_OAUTH_CLIENT_ID = environ.get("GITHUB_OAUTH_CLIENT_ID")
#GITHUB_OAUTH_CLIENT_SECRET = environ.get("GITHUB_OAUTH_CLIENT_SECRET")

#app.config['SESSION_TYPE'] = 'filesystem'
#app.config["SECRET_KEY"] = FLASK_SECRET_KEY
#app.config.update(
#    TESTING=True,


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mariadb

##engine = sqlalchemy.create_engine("mariadb+mariadbconnector://app_user:Password123!@127.0.0.1:3306/company")

MARIADB_USERNAME = environ.get("MARIADB_USERNAME")
MARIADB_PASSWORD = environ.get("MARIADB_PASSWORD")
MARIADB_DATABASE = environ.get("MARIADB_DATABASE")

MARIADB_URI = "mariadb+mariadbconnector://" + MARIADB_USERNAME + ":" + MARIADB_PASSWORD + "@localhost:3306/" + MARIADB_DATABASE

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'

print(MARIADB_URI)

app.config['SQLALCHEMY_DATABASE_URI'] = MARIADB_URI

db = SQLAlchemy(app)

## /run/mysqld/mysqld.sock ## maria db container

