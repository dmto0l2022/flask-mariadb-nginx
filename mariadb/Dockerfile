#docker run --detach
#--name some-mariadb
#--env MARIADB_USER=example-user
#--env MARIADB_PASSWORD=my_cool_secret
#--env MARIADB_ROOT_PASSWORD=my-secret-pw  
#mariadb:latest

FROM mariadb:latest

#ADD sql/ /docker-entrypoint-initdb.d

#ENV MYSQL_ROOT_PASSWORD test123
#ENV MYSQL_DATABASE testDB
#ENV MYSQL_USER toto
#ENV MYSQL_PASSWORD test123

env MARIADB_USER=pythonuser
env MARIADB_PASSWORD=pythonuser
env MARIADB_ROOT_PASSWORD=pythonuser
env MARIADB_DATABASE=world

RUN apt-get update && apt-get -y install vim
RUN apt-get -y install unzip

COPY world-db.zip /var/www/html/world-db.zip
RUN unzip -j /var/www/html/world-db.zip -d /docker-entrypoint-initdb.d

#unzip -j /path/to/file.zip -d other_folder

RUN rm /var/www/html/world-db.zip

COPY init.sql /docker-entrypoint-initdb.d/init.sql

EXPOSE 3306

CMD ["mysqld"]

#RUN wget -O /var/www/html/type.zip http://wp-templates.ru/download/2405 \
#&& unzip '/var/www/html/type.zip' -d /var/www/html/wp-content/themes/ && rm 
#/var/www/html/type.zip || true;

#ADD 20211104_dmtools_backup.sql /docker-entrypoint-initdb.d

