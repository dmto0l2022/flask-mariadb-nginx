import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")

#"mariadb+mariadbconnector://" + MARIADB_USERNAME + ":" + MARIADB_PASSWORD + "@localhost:3306/" + MARIADB_DATABASE

engine_string = "mariadb+mariadbconnector://pythonuser:pythonuser@mariadb1:3306/mysql"


#engine = create_engine("mysql+pymysql://sylvain:passwd@localhost/db",
#                       connect_args= dict(host='localhost', port=3306))

#engine = create_engine(engine_string, connect_args= dict(host='localhost', port=3306))

#app.config['SQLALCHEMY_DATABASE_URI'] = ''mysql://dayenu:secret.word@localhost/dayenu?unix_socket=/usr/local/mysql5/mysqld.sock

#engine_string = "mariadb+mariadbconnector://pythonuser:pythonuser@localhost/world?unix_socket=/run/mysqld/mysqld.sock"

#127.0.0.1

engine = create_engine(engine_string)

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    last_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
 
Base.metadata.create_all(engine)

