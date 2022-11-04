FROM python:3
ADD app.py /
ADD .env /
RUN pip install flask
RUN pip install flask_restful
RUN pip install Flask-Dance[sqla]

EXPOSE 5000
CMD [ "python", "./app.py"]
