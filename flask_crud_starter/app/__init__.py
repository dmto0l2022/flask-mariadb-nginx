from flask import Flask
from database_bind import SQLAlchemy_bind

# outside of app factory
db = SQLAlchemy_bind()

# must be defined after db = SQLAlchemy_bind() if in same module
from sqlalchemy import Column, Integer, String
class User(db.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String, unique=True)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

# app factory
def create_app():
    app = Flask(__name__)
    app.config["DATABASE"] = "sqlite:///:memory:"
    # import your database tables if defined in a different module
    # for example if the User model above was in a different module:
    from your_application.database import User
    db.init_app(app)
    return app
