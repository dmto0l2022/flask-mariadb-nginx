"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database setup
db = SQLAlchemy()


def init_app():
    """Create Flask application."""
    flask_app = Flask(__name__, instance_relative_config=False)

    flask_app.config.from_object('app.config.Config')  # configure app using the Config class defined in src/config.py

    db.init_app(flask_app)  # initialise the database for the app

    with flask_app.app_context():
        from app.models import User  # this import allows us to create the table if it does not exist
        db.create_all()

        from app.blueprints.users import users_bp
        flask_app.register_blueprint(users_bp)

        return flask_app
