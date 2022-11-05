FROM python:3

RUN curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash

RUN apt-get update && apt-get install -y mariadb-server galera-4 mariadb-client libmariadb3 mariadb-backup mariadb-common

ADD minimal_app.py /
ADD app.py /
ADD b2b.py /
ADD .env /
RUN pip install flask
RUN pip install SQLAlchemy
RUN pip install flask_restful
RUN pip install flask_sqlalchemy
RUN pip install Flask-Dance[sqla]
RUN pip install python-dotenv
RUN pip install mariadb

##RUN touch /run/mysqld/mysqld.sock
##RUN touch /run/mysqld/mysqld.pid

EXPOSE 5000
CMD [ "python", "./b2b.py"]
