# model.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from . import db ## import db from __init__

# must be defined after db = SQLAlchemy_bind() if in same module
# from sqlalchemy import Column, Integer, String

class User(db.Base):
    __tablename__ = 'users_new'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    password = Column(String(25), unique=True)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

# User table
class UserSimple(db.Base):
    __tablename__ = "users_simple"
    id = Column(Integer, primary_key=True)
    username = Column(String(25))
    name = Column(String(25))
    email = Column(String(25))

    def __init__(self, username: str, name: str, email: str):
        self.username = username
        self.name = name
        self.email = email

    @staticmethod
    def create(username, name, email):
        """
        Create new user
        """
        new_user = User(username, name, email)
        db.Base.session.add(new_user)
        db.Base.session.commit()

    @staticmethod
    def get_users():
        """
        :return: list of user details
        """
        users = [
            {
                'user_id': i.id,
                'username': i.username,
                'name': i.name,
                'email': i.email,
            }
            for i in User.query.order_by('id').all()
        ]
        return users

# Plots table
class Plots(db.Base):
    __tablename__ = "plots"
    id = Column(Integer, primary_key=True)
    plotid = Column(String(25))
    name = Column(String(25))

    def __init__(self, plotid: str, name: str):
        self.plotid = plotid
        self.name = name

    @staticmethod
    def create(plotid,name):
        """
        Create new plot
        """
        new_plots = Plots(plotid,name)
        db.Base.session.add(new_plots)
        db.Base.session.commit()

    @staticmethod
    def get_plots():
        """
        :return: list of user details
        """
        plots = [
            {
                'id': i.id,
                'plotid': i.plotid,
                'name': i.name,
            }
            for i in Plots.query.order_by('id').all()
        ]
        return plots
