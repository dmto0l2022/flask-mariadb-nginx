FROM mysql:latest
MAINTAINER andrew@gaitskell.com

ENV MYSQL_ROOT_PASSWORD pythonuser


ENV MYSQL_DATABASE=RubyDB
ENV MYSQL_USER=pythonuser
ENV MYSQL_PASSWORD=pythonuser


COPY init.sql /docker-entrypoint-initdb.d/init.sql
ADD 20211104_dmtools_backup.sql /docker-entrypoint-initdb.d

EXPOSE 3306
