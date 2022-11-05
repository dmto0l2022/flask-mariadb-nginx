FROM python:3

RUN apt-get install gcc
RUN apt-get install python3-dev

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
