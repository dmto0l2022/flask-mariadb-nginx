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

WORKDIR /workdir

ARG USERNAME=agaitske
ARG PASSWD=test
ARG USER_UID=1001
ARG USER_GID=1002 ## dm group

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN echo "${USER_UID}:${PASSWD}" | chpasswd

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
