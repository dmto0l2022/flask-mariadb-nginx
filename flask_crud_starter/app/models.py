# model.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

#Base = declarative_base()

from app.database import AppDb
app_db = AppDb()



# User table
class User(Base):
    __tablename__ = "users_simple"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)
    email = Column(String)

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
        Base.session.add(new_user)
        Base.session.commit()

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
