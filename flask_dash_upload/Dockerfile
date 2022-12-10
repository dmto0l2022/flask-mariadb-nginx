FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


RUN apt-get update && apt-get -y install vim
RUN apt-get -y install unzip

ARG USERNAME=agaitske
ARG USER_UID=1001
ARG USER_GID=1002 ## dm group

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

#RUN mkdir /docker-entrypoint-initdb.d ## already exists
RUN chown $USER_UID:$USER_GID /docker-entrypoint-initdb.d
RUN chown $USER_UID:$USER_GID /var/lib/mysql

USER $USERNAME
#ADD sql/ /docker-entrypoint-initdb.d


COPY world-db.zip /var/www/html/world-db.zip
RUN unzip -j /var/www/html/world-db.zip -d /docker-entrypoint-initdb.d

#RUN unzip -j /var/www/html/world-db.zip -d /

COPY x_backup.sql /docker-entrypoint-initdb.d

#unzip -j /path/to/file.zip -d other_folder

#RUN rm /var/www/html/world-db.zip

COPY init.sql /docker-entrypoint-initdb.d/init.sql

EXPOSE 3306

CMD ["mysqld"]
