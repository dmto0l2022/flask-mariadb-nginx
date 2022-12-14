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

####

RUN mkdir -p /workdir/config
RUN mkdir -p /workdir/config/systemd
RUN mkdir -p /workdir/config/systemd/user

COPY podman.socket /workdir/config/systemd/user/podman.socket
COPY podman.service /workdir/config/systemd/user/podman.service

RUN mkdir -p /workdir/config/containers
RUN mkdir -p /workdir/config/containers/user

COPY storage.conf /workdir/config/containers/user/storage.conf
COPY storage.conf /workdir/config/containers/user/registries.conf

RUN ln -s /etc/containers/registries.conf  /workdir/config/containers/user/registries.conf

RUN systemctl --user daemon-reload
RUN systemctl --user enable --now podman.socket

RUN export DOCKER_HOST=unix://$HOME/podman.sock
RUN export CONTAINER_HOST=unix://$HOME/podman.sock

####

WORKDIR /workdir

RUN mkdir /workdir/home

##RUN addgroup shadow \
RUN chgrp shadow /etc/shadow \
    &&  chmod g+r /etc/shadow

ARG user=jupyterhub
ARG home=/workdir/home/$user
RUN addgroup --system docker
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home $home \
    --ingroup docker \
    $user

RUN echo "jupyterhub:jupyterhub" | chpasswd

ARG USERNAME=agaitske
ARG USER_UID=1001
ARG USER_GID=1002 ## dm group

# Create the main user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -g shadow -m $USERNAME

## last one above allows access to passwords

# Add jupyterhub user to dm group
RUN usermod -a -G $USER_GID $user

#RUN mkdir /docker-entrypoint-initdb.d ## already exists
#RUN chown $USER_UID:$USER_GID /docker-entrypoint-initdb.d
#RUN chown $USER_UID:$USER_GID /var/lib/mysql
RUN chown $USER_UID:$USER_GID /workdir

RUN mkdir /workdir/uploads
RUN chown $USER_UID:$USER_GID /workdir/uploads

RUN mkdir /workdir/notebooks
RUN chown $USER_UID:$USER_GID /workdir/notebooks

RUN mkdir /workdir/jupyterhub
RUN chown $USER_UID:$USER_GID /workdir/jupyterhub

USER $USERNAME

RUN npm install -g configurable-http-proxy

RUN mkdir "${HOME}/.npm-packages"
RUN npm config set prefix "${HOME}/.npm-packages"
RUN export PATH="$PATH:${HOME}/.npm-packages/bin"
RUN npm install -g configurable-http-proxy

ENV VIRTUAL_ENV=/workdir/env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt /workdir/requirements.txt
RUN /workdir/env/bin/pip install -r /workdir/requirements.txt

#RUN jupyter lab build

RUN /workdir/env/bin/pip -q install pip --upgrade
RUN /workdir/env/bin/pip install wheel

RUN /workdir/env/bin/pip install git+https://github.com/manics/podmanclispawner

#RUN touch jupyterhub_cookie_secret
#RUN chmod g+rw jupyterhub_cookie_secret
#RUN openssl rand -hex 32 > jupyterhub_cookie_secret
#RUN chmod 600 jupyterhub_cookie_secret

#RUN /workdir/env/bin/python jupyterhub --generate-config

#RUN /workdir/env/bin/activate && exec jupyterhub --generate-config

#COPY . .
COPY jupyterhub_config.py /workdir/jupyterhub/jupyterhub_config.py
EXPOSE 8000
#CMD . /srv/jupyterhub/env/bin/activate && exec jupyterhub
CMD . /workdir/env/bin/activate & exec jupyterhub -f /workdir/jupyterhub/jupyterhub_config.py

