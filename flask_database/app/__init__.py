from flask import Flask
import mariadb
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#gh
##>> from flask_dance.contrib.github import make_github_blueprint, github
##from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage
from flask_dance.consumer import oauth_authorized, oauth_error

from flask_security import Security, SQLAlchemyUserDatastore, auth_required, hash_password
from flask_security.models import fsqla_v3 as fsqla

#from app.oauth import github_blueprint

from flask_login import LoginManager

#from config import Config

import os

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

## while testing without https
##>> os.environ["OAUTHLIB_INSECURE_TRANSPORT"]="1"

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    
    db = SQLAlchemy()
        
    print('key from file: ')
    print(environ.get('FLASK_SECRET_KEY'))

    app.config['SECRET_KEY'] = environ.get('FLASK_SECRET_KEY')
    ##gh
    
    ##>> GITHUB_OAUTH_CLIENT_ID = environ.get("GITHUB_OAUTH_CLIENT_ID")
    ##>> GITHUB_OAUTH_CLIENT_SECRET = environ.get("GITHUB_OAUTH_CLIENT_SECRET")
    
    #github_blueprint = make_github_blueprint(
    #            client_id=GITHUB_OAUTH_CLIENT_ID,
    #            client_secret=GITHUB_OAUTH_CLIENT_SECRET,
    #            )
    
    #app.register_blueprint(github_blueprint, url_prefix="/login")
    ##gh
    
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

    #db = SQLAlchemy(app)

    login = LoginManager(app)
    
    login.login_view = 'login'
    ##>> login.login_view = 'github.login'
    
    db.init_app(app)

    # setup SQLAlchemy backend
    #blueprint.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user)
    ##SQLAlchemyStorage
    #github_blueprint.backend = SQLAlchemyStorage(OAuth, db.session, user=current_user)
    
    migrate = Migrate(app, db, login)
    
    
    with app.app_context():
        #app.config["APPLICATION_ROOT"] = "/app"
        #SCRIPT_NAME
        #app.config["SCRIPT_NAME"] = "/app"
        ##>> from . import routes, models, oauth  # Import routes, models and oauth helper
        from . import routes, models 
        #from models import db, login_manager
        #from oauth import github_blueprint
        
        ##>> app.register_blueprint(oauth.github_blueprint, url_prefix="/app/login")
        
        db.Model.metadata.reflect(db.engine)
        
        db.create_all()  # Create sql tables for our data models
        db.session.commit()
        print("Database tables created")
        #from app.models import User, Post
        #app.app_context().push()
        #u = User(username='john', email='john@example.com')
        #db.session.add(u)
        #db.session.commit()
        return app




##from app import routes, models
'''if __name__ == "__main__":
    if "--setup" in sys.argv:
        with app.app_context():
            db.create_all()
            db.session.commit()
            print("Database tables created")
    else:
        app.run(debug=True)
'''

print("finished")
