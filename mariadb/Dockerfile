#docker run --detach
#--name some-mariadb
#--env MARIADB_USER=example-user
#--env MARIADB_PASSWORD=my_cool_secret
#--env MARIADB_ROOT_PASSWORD=my-secret-pw  
#mariadb:latest

ARG ENV_UID=me

FROM mariadb:latest

RUN apt-get update && apt-get -y install vim
RUN apt-get -y install unzip

ARG USERNAME=agaitske
##ARG USER_UID=1001
ARG USER_UID=${ENV_UID}
ARG USER_GID=1002 ## dm group

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

#RUN mkdir /docker-entrypoint-initdb.d ## already exists
RUN chown $USER_UID:$USER_GID /docker-entrypoint-initdb.d
RUN chown $USER_UID:$USER_GID /var/lib/mysql

USER $USERNAME
#ADD sql/ /docker-entrypoint-initdb.d

#ENV MYSQL_ROOT_PASSWORD test123
#ENV MYSQL_DATABASE testDB
#ENV MYSQL_USER toto
#ENV MYSQL_PASSWORD test123

env MARIADB_USER=pythonuser
#env MARIADB_USER=root
env MARIADB_PASSWORD=pythonuser
env MARIADB_ROOT_PASSWORD=pythonuser
#env MARIADB_DATABASE=RubyDB
env MARIADB_DATABASE=world
#env MARIADB_MULTIPLE_DATABASES=RubyDB,world


COPY world-db.zip /var/www/html/world-db.zip
RUN unzip -j /var/www/html/world-db.zip -d /docker-entrypoint-initdb.d

#RUN unzip -j /var/www/html/world-db.zip -d /

### COPY x_backup.sql /docker-entrypoint-initdb.d

#unzip -j /path/to/file.zip -d other_folder

#RUN rm /var/www/html/world-db.zip

COPY init.sql /docker-entrypoint-initdb.d/init.sql

EXPOSE 3306

CMD ["mysqld"]

