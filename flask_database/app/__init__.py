from flask import Flask

#from config import Config

import os

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

app = Flask(__name__)
app.config['FLASK_SECRET'] = "a"

from app import routes
