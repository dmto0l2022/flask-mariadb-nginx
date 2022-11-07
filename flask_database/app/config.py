import os

from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

##engine = sqlalchemy.create_engine("mariadb+mariadbconnector://app_user:Password123!@127.0.0.1:3306/company")


##MARIADB_URI = "mariadb+mariadbconnector://" + MARIADB_USERNAME + ":" + MARIADB_PASSWORD + "@localhost:3306/" + MARIADB_DATABASE


class Config(object):
    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MARIADB_USERNAME = environ.get("MARIADB_USERNAME")
    MARIADB_PASSWORD = environ.get("MARIADB_PASSWORD")
    MARIADB_DATABASE = environ.get("MARIADB_DATABASE")

