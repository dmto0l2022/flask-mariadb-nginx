FROM python:3
ADD app_simple.py /
ADD myapp.py /
ADD /app/*.* /app/
ADD /app/templates/*.* /app/templates/
RUN pip install python-dotenv
RUN pip install flask
RUN pip install flask_restful
RUN pip install flask-wtf
RUN pip install flask-sqlalchemy
RUN pip install flask-migrate
RUN flask db init
# EXPOSE 5000
##CMD [ "python", "./app_simple.py"]
CMD [ "python", "./myapp.py"]
