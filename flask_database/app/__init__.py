from flask import Flask
import mariadb
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

MARIADB_USERNAME = environ.get("MARIADB_USERNAME")
MARIADB_PASSWORD = environ.get("MARIADB_PASSWORD")
MARIADB_DATABASE = environ.get("MARIADB_DATABASE")
MARIADB_CONTAINER = environ.get("MARIADB_CONTAINER")
##MARIADB_CONTAINER = "mariadb_backend-1"

#MARIADB_CONTAINER = "10.154.0.18"
#MARIADB_CONTAINER = "10.154.0.20" ## internal IP address of the VM server
#MARIADB_CONTAINER = "localhost"

MARIADB_URI = "mariadb+mariadbconnector://" + MARIADB_USERNAME + ":" + MARIADB_PASSWORD + "@" + MARIADB_CONTAINER + ":3306/" + MARIADB_DATABASE

app.config['SQLALCHEMY_DATABASE_URI'] = MARIADB_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

print("finished")
