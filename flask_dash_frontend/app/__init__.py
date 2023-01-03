from flask import Flask
from flask import flash
from flask_session import Session
from . import database_bind as dbind

# outside of app factory
db = dbind.SQLAlchemy_bind()

import os
from os import environ, path

from dotenv import load_dotenv

import secrets
import string

import random

# initializing size of string
N = 32
 
# using secrets.choice()
# generating random strings
#res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
#              for i in range(N))

res = ''.join(random.choices(string.ascii_letters, k=N))

# print result
print("The generated random string : " + str(res))

#os.environ["SECRET_KEY"] = os.urandom(32)
os.environ["SECRET_KEY"] = res

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

print('BASE_DIR')
print(BASE_DIR)

'''
# must be defined after db = SQLAlchemy_bind() if in same module
from sqlalchemy import Column, Integer, String

class User(db.Base):
    __tablename__ = 'users_new'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    password = Column(String(25), unique=True)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
'''

# app factory
def init_app():
    MARIADB_USERNAME = environ.get("MARIADB_USERNAME")
    MARIADB_PASSWORD = environ.get("MARIADB_PASSWORD")
    MARIADB_DATABASE = environ.get("MARIADB_DATABASE")
    MARIADB_CONTAINER = environ.get("MARIADB_CONTAINER")
    
    #FLASK_SECRET_KEY = environ.get("FLASK_SECRET_KEY") ## from file
    FLASK_SECRET_KEY = environ.get("SECRET_KEY") ## generated

    MARIADB_URI = "mariadb+mariadbconnector://" + MARIADB_USERNAME + ":" + \
                    MARIADB_PASSWORD + "@" + MARIADB_CONTAINER + ":3306/"\
                    + MARIADB_DATABASE
    print(MARIADB_URI)
    app = Flask(__name__)
    filename = os.path.join(app.instance_path, 'my_folder', 'my_file.txt')
    print('filename')
    print(filename)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = FLASK_SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = MARIADB_URI
    ###
    ## session
    # Configure Redis for storing the session data on the server-side
   
      
    
    # import your database tables if defined in a different module
    from . import models
    # for example if the User model above was in a different module:
    db.init_app(app)
    
    ## setup session data
    #app.config['SESSION_TYPE'] = 'sqlalchemy'
    #app.config['SESSION_PERMANENT'] = False
    #app.config['SESSION_USE_SIGNER'] = True
    #app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions'
    #app.config['SESSION_SQLALCHEMY'] = db
    #server_session = Session(app)
   

    #server_session.app.session_interface.db.create_all()

    
    from app.blueprints.home_bp import home_bp
    app.register_blueprint(home_bp)
    from app.blueprints.plotids_bp import plotids_bp
    app.register_blueprint(plotids_bp)
    ##
    #dashapp1_bp
    from app.blueprints.dashapp1_bp import dashapp1_bp
    app.register_blueprint(dashapp1_bp)
    ##
    ##todo_bp
    from app.blueprints.todo_bp import todo_bp
    app.register_blueprint(todo_bp)
    
    ##session_bp
    from app.blueprints.session_bp import session_bp
    app.register_blueprint(session_bp)
    
    return app
