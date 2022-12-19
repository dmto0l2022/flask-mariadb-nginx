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

# At top of file
from flask_mail import Mail
from werkzeug.middleware.proxy_fix import ProxyFix





#from app.oauth import github_blueprint

## from flask_login import LoginManager

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
    
    # required for user logging
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)
    
    db = SQLAlchemy()
        
    print('key from file: ')
    print(environ.get('FLASK_SECRET_KEY'))

    app.config['SECRET_KEY'] = environ.get('FLASK_SECRET_KEY')
    ##security
    
    app.config['SECURITY_PASSWORD_SALT'] = environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')

    # have session and remember cookie be samesite (flask/flask_login)
    app.config["REMEMBER_COOKIE_SAMESITE"] = "strict"
    app.config["SESSION_COOKIE_SAMESITE"] = "strict"
    
    
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
    
    ##security
    
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_pre_ping": True,
    }
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    ##
    
    
    #login = LoginManager(app)
    
    #login.login_view = 'login'
    ##>> login.login_view = 'github.login'
    
    db.init_app(app)

    # setup SQLAlchemy backend
    #blueprint.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user)
    ##SQLAlchemyStorage
    #github_blueprint.backend = SQLAlchemyStorage(OAuth, db.session, user=current_user)
    
    
    ##migrate = Migrate(app, db, login)
    migrate = Migrate(app, db)
    
    with app.app_context():
        #app.config["APPLICATION_ROOT"] = "/app"
        #SCRIPT_NAME
        #app.config["SCRIPT_NAME"] = "/app"
        ##>> from . import routes, models, oauth  # Import routes, models and oauth helper
        from . import routes, models 
        #from models import db, login_manager
        #from oauth import github_blueprint
        
        ##https://stackoverflow.com/questions/14793098/how-to-use-flask-security-register-view
        app.config['SECURITY_REGISTERABLE'] = True
        app.config['SECURITY_REGISTER_URL'] = '/app/register'
        app.config['SECURITY_LOGIN_URL'] = '/app/login'
        app.config['SECURITY_LOGOUT_URL'] = '/app/logout'
        app.config['SECURITY_RESET_URL'] = '/app/reset'
        app.config['SECURITY_CHANGE_URL'] = '/app/change'
        app.config['SECURITY_CONFIRM_URL'] = '/app/confirm'
        app.config['SECURITY_POST_LOGIN_VIEW'] = '/app/welcome'
        app.config['SECURITY_POST_LOGOUT_VIEW'] = '/app/login'
        app.config['SECURITY_POST_REGISTER_VIEW'] = '/app/welcome'
        app.config['SECURITY_POST_CONFIRM_VIEW'] = '/app/welcome'
        app.config['SECURITY_POST_RESET_VIEW'] = '/app/welcome'
        app.config['SECURITY_POST_CHANGE_VIEW'] = '/app/welcome'
        app.config['SECURITY_UNAUTHORIZED_VIEW'] = '/app/register'
        app.config['SECURITY_CONFIRMABLE'] = True
        app.config['SECURITY_RECOVERABLE'] = True
        app.config['SECURITY_TRACKABLE='] = True
        app.config['SECURITY_CHANGEABLE'] = True
        
        # Setup Flask-Security
        user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
        app.security = Security(app, user_datastore)
        
        mail = Mail(app)
        
        app.security.datastore.db.create_all()
        #if not app.security.datastore.find_user(email="test@me.com"):
        #    app.security.datastore.create_user(email="test@me.com", password=hash_password("password"))
        app.security.datastore.db.session.commit()
        
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
