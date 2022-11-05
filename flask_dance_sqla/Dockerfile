FROM python:3

RUN curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash
RUN apt-get update

RUN apt-get install mariadb-client libmariadb3
ADD minimal_app.py /
ADD .env /
RUN pip install flask
RUN pip install flask_restful
RUN pip install flask_sqlalchemy
RUN pip install Flask-Dance[sqla]
RUN pip install python-dotenv
RUN pip install mariadb


EXPOSE 5000
CMD [ "python", "./minimal_app.py"]
