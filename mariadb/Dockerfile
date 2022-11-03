FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y mariadb-server

EXPOSE 3306

LABEL version="1.0"
LABEL description="MariaDB Server"

MAINTAINER andrew@gaitskell.com

ENV MYSQL_ROOT_PASSWORD pythonuser


ENV MYSQL_DATABASE=RubyDB
ENV MYSQL_USER=pythonuser
ENV MYSQL_PASSWORD=pythonuser


#RUN wget -O /var/www/html/type.zip http://wp-templates.ru/download/2405 \
#&& unzip '/var/www/html/type.zip' -d /var/www/html/wp-content/themes/ && rm 
#/var/www/html/type.zip || true;

COPY world.zip /var/www/html/world.zip
RUN unzip '/var/www/html/type.zip'

COPY init.sql /docker-entrypoint-initdb.d/init.sql
ADD 20211104_dmtools_backup.sql /docker-entrypoint-initdb.d

EXPOSE 3306
