# RHEL notes

## good code comments

https://medium.com/@lyle-okoth/how-to-authenticate-and-register-a-user-using-flask-dance-and-the-github-oauth-api-a5aa64edc64b

## flask needs to know it is behind a proxy

https://flask.palletsprojects.com/en/latest/deploying/proxy_fix/

https://flask.palletsprojects.com/en/latest/deploying/nginx/

## to allow access to html folder

      setenforce Permissive

# Reference & Thanks

## todo tomorrow

https://pypi.org/project/Flask-Dance/

## book mark

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms

## generate model

            https://stackoverflow.com/questions/51416482/flask-application-unable-to-run-because-of-keyerror

            hostname -I

             10.154.0.24

            pip install sqlacodegen
            pip install flask-sqlacodegen


            sqlacodegen  mariadb+mariadbconnector://user:password@10.154.0.24:3306/world > mymodel.py

# other workings

            import os
            from os import environ, path

            from dotenv import load_dotenv

            BASE_DIR = path.abspath(path.dirname(__file__))
            load_dotenv(path.join(BASE_DIR, ".env"))

            ####  https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

            #FLASK_DEBUG = environ.get("FLASK_DEBUG")
            #FLASK_SECRET_KEY = environ.get("FLASK_SECRET_KEY")
            #GITHUB_OAUTH_CLIENT_ID = environ.get("GITHUB_OAUTH_CLIENT_ID")
            #GITHUB_OAUTH_CLIENT_SECRET = environ.get("GITHUB_OAUTH_CLIENT_SECRET")

            #app.config['SESSION_TYPE'] = 'filesystem'
            #app.config["SECRET_KEY"] = FLASK_SECRET_KEY
            #app.config.update(
            #    TESTING=True,


            from flask import Flask
            from flask_sqlalchemy import SQLAlchemy
            import mariadb

            ##engine = sqlalchemy.create_engine("mariadb+mariadbconnector://app_user:Password123!@127.0.0.1:3306/company")

            MARIADB_USERNAME = environ.get("MARIADB_USERNAME")
            MARIADB_PASSWORD = environ.get("MARIADB_PASSWORD")
            MARIADB_DATABASE = environ.get("MARIADB_DATABASE")

            MARIADB_URI = "mariadb+mariadbconnector://" + MARIADB_USERNAME + ":" + MARIADB_PASSWORD + "@localhost:3306/" + MARIADB_DATABASE

            app = Flask(__name__)
            #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'

            print(MARIADB_URI)

            app.config['SQLALCHEMY_DATABASE_URI'] = MARIADB_URI

            db = SQLAlchemy(app)

            print("finished")

# previous success

      import sqlalchemy
      from sqlalchemy import create_engine
      from sqlalchemy.ext.declarative import declarative_base

      #engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")

      #"mariadb+mariadbconnector://" + MARIADB_USERNAME + ":" + MARIADB_PASSWORD + "@localhost:3306/" + MARIADB_DATABASE

      engine_string = "mariadb+mariadbconnector://root:pythonuser@mariadb1:3306/world"


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

      print(engine.table_names())

      print("finished")
