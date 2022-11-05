import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")

#"mariadb+mariadbconnector://" + MARIADB_USERNAME + ":" + MARIADB_PASSWORD + "@localhost:3306/" + MARIADB_DATABASE

engine_string = "mariadb+mariadbconnector://pythonuser:pythonuser@localhost:3306/world"

engine = create_engine(engine_string)

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    last_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
 
Base.metadata.create_all(engine)

