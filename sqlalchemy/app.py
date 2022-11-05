import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import mariadb
engine_string = "mariadb+mariadbconnector://pythonuser:pythonuser@dev2.dmtools.info:3306/world"
engine = create_engine(engine_string)
Base = declarative_base()
class Employee(Base):
    __tablename__ = 'employees'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    last_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
Base.metadata.create_all(engine)
