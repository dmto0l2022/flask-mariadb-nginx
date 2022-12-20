
import os

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

mail_server = environ.get('MAIL_SERVER')
mail_port = environ.get('MAIL_PORT')
mail_username = environ.get('MAIL_USERNAME')
mail_password = environ.get('MAIL_PASSWORD')
sender_email = environ.get('MAIL_SENDEREMAIL')
receiver_email = environ.get('MAIL_RECEIVEREMAIL')

# After 'Create app'
app.config['MAIL_SERVER'] = mail_server
app.config['MAIL_PORT'] = mail_port
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

## https://stackoverflow.com/questions/65997108/flask-mail-ssl-wrong-version-number-wrong-version-number-ssl-c1123
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
