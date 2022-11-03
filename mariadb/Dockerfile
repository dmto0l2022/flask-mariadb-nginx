#docker run --detach
#--name some-mariadb
#--env MARIADB_USER=example-user
#--env MARIADB_PASSWORD=my_cool_secret
#--env MARIADB_ROOT_PASSWORD=my-secret-pw  
#mariadb:latest


FROM mariadb:latest

EXPOSE 3306

LABEL version="1.0"
LABEL description="MariaDB Server"

MAINTAINER andrew@gaitskell.com

env MARIADB_USER=pythonuser
env MARIADB_PASSWORD=pythonuser
env MARIADB_ROOT_PASSWORD=pythonuser
env MARIADB_DATABASE=RubyDB

RUN apt install unzip

#RUN wget -O /var/www/html/type.zip http://wp-templates.ru/download/2405 \
#&& unzip '/var/www/html/type.zip' -d /var/www/html/wp-content/themes/ && rm 
#/var/www/html/type.zip || true;

COPY world-db.zip /var/www/html/world-db.zip
RUN unzip /var/www/html/world-db.zip -d /docker-entrypoint-initdb.d
RUN rm /var/www/html/world-db.zip

COPY init.sql /docker-entrypoint-initdb.d/init.sql
#ADD 20211104_dmtools_backup.sql /docker-entrypoint-initdb.d

