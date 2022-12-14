FROM python:3

#FROM ubuntu:latest
RUN apt-get update && apt-get -y update \
    && apt-get -y install openssl \
    && apt-get -y install sudo \
    && apt-get install -y apt-utils dialog \
    && apt-get install -y build-essential python3.10 python3-pip python3-dev \
    && apt-get -y install nodejs npm \
    && apt-get -y install podman

RUN curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash
RUN apt-get update && apt-get install -y mariadb-server galera-4 mariadb-client libmariadb3 mariadb-backup mariadb-common
RUN apt-get install libmariadb-dev

RUN npm install -g configurable-http-proxy

# Install dockerspawner, nativeauthenticator
#RUN python3 -m pip install --no-cache-dir \
 #       dockerspawner==12.* \
  #      jupyterhub-nativeauthenticator==1.*

WORKDIR /workdir
#RUN mkdir /workdir
RUN mkdir /workdir/jupyterhub

COPY jupyterhub_config.py /workdir/jupyterhub/jupyterhub_config.py
COPY requirements.txt /workdir/jupyterhub/requirements.txt
RUN python3 -m pip install --no-cache-dir -r /workdir/jupyterhub/requirements.txt

RUN ls -al /workdir/jupyterhub/

CMD ["jupyterhub", "-f", "/workdir/jupyterhub/jupyterhub_config.py"]

##CMD ["sh", "-c", "jupyter notebook --port=8889 --no-browser --ip=*"]

