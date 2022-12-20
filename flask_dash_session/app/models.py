from . import database as dbf # import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
                    String, ForeignKey, UnicodeText

class User(dbf.Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    fs_uniquifier = Column(String(255), unique=True, nullable=False)
    confirmed_at = Column(DateTime())
    
