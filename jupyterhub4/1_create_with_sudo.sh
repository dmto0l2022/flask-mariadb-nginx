#!/bin/sh
MY_MESSAGE="Hello World"
echo $MY_MESSAGE

OME="/workdir/home/jupyterhub"

FROM python:3

apt-get update && apt-get -y update
apt-get -y install openssl
#apt-get -y install sudo
apt-get install -y apt-utils dialog
apt-get install -y build-essential python3.10 python3-pip python3-dev
apt-get -y install nodejs npm

curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash
apt-get update
apt-get install -y mariadb-server galera-4 mariadb-client libmariadb3 mariadb-backup mariadb-common
apt-get install libmariadb-dev

mkdir /workdir
mkdir /workdir/home

chgrp shadow /etc/shadow \
    &&  chmod g+r /etc/shadow

user="agaitske"
home="/workdir/home/agaitske"
addgroup jupyterhub

#usermod -a -G examplegroup exampleusername
usermod -a -G jupyterhub agaitske

#chown [OPTIONS] USER[:GROUP] FILE(s)
mkdir /workdir/notebooks
chown agaitske:jupyterhub /workdir/notebooks

mkdir /workdir/jupyterhub
chown agaitske:jupyterhub /workdir/jupyterhub

RUN chmod -R 2775 /workdir/
