FROM python:3

RUN curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash
RUN apt-get update && apt-get install -y mariadb-server galera-4 mariadb-client libmariadb3 mariadb-backup mariadb-common
ADD entry-point.sh /
ADD app_simple.py /
ADD myapp.py /
ADD wsgi.py /
ADD /app/*.* /app/
ADD /app/templates/*.* /app/templates/
RUN pip install python-dotenv
RUN pip install flask
RUN pip install flask_restful
RUN pip install flask-wtf
RUN pip install flask-sqlalchemy
RUN pip install flask-migrate
RUN pip install mariadb
RUN pip install Flask-Dance[sqla]
#RUN flask db init
#RUN flask db migrate -m "users table"
#RUN flask db upgrade
# EXPOSE 5000
##CMD [ "python", "./app_simple.py"]
#CMD [ "python", "./myapp.py"]
RUN chmod +x /entry-point.sh
ENTRYPOINT ["./entry-point.sh"]
