import os

from flask import Flask, render_template_string

from . import database as dbf ##import db_session, init_db
from . import models as modf ## import User, Role

import mariadb

from werkzeug.middleware.proxy_fix import ProxyFix

import os

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

def create_app():
     # Create app
     app = Flask(__name__)
     app.config['DEBUG'] = True

     # Generate a nice key using secrets.token_urlsafe()
     app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
     # Bcrypt is set as default SECURITY_PASSWORD_HASH, which requires a salt
     # Generate a good salt using: secrets.SystemRandom().getrandbits(128)
     #app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')

     with app.app_context():
        #app.config["APPLICATION_ROOT"] = "/app"
        #SCRIPT_NAME
        #app.config["SCRIPT_NAME"] = "/app"
        ##>> from . import routes, models, oauth  # Import routes, models and oauth helper
        from . import routes ## models
        
        # Create a user to test with
        d = dbf.init_db()
        dbf.db_session.commit()
        
        # create session and add objects
        # verbose version of what a context manager will do
        with dbf.Session(dbf.engine) as session:
            session.begin()
            try:
               #session.add(some_object)
               #session.add(some_other_object)
               user1 = User(name="user1")
               user2 = User(name="user2")
               session.add(user1)
               session.add(user2)
               session.commit()
            except:
               session.rollback()
               raise
            else:
               session.commit()
          
        with dbf.Session(dbf.engine) as session:
              # query for ``User`` objects
              statement = select(User).filter_by(name="user1")

              # list of ``User`` objects
              user_obj = session.scalars(statement).all()

              # query for individual columns
              statement = select(User.name)

              # list of Row objects
              rows = session.execute(statement).all()
              print(rows)
               
        return app
