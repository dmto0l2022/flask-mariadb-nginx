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

RUN mkdir srv/jupyterhub
RUN mkdir srv/jupyterhub/home

RUN mkdir srv/jupyterhub/notebooks

ARG user=jupyterhub
ARG home=/srv/jupyterhub/home/$user
RUN addgroup --system docker
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home $home \
    --ingroup docker \
    $user


RUN usermod -aG shadow jupyterhub

RUN echo "jupyterhub:jupyterhub" | chpasswd

RUN usermod -aG sudo jupyterhub

RUN groupadd jupyterhub

RUN usermod -aG jupyterhub jupyterhub

RUN chown -R jupyterhub:jupyterhub /srv/jupyterhub

#ensures that /var/run/docker.sock exists
#RUN touch /var/run/docker.sock

#changes the ownership of /var/run/docker.sock
#RUN chown jupyterhub:jupyterhub /var/run/docker.sock

RUN chown jupyterhub .

USER jupyterhub

ENV VIRTUAL_ENV=/srv/jupyterhub/env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN jupyter lab build

RUN pip -q install pip --upgrade
RUN pip install wheel

RUN pip install git+https://github.com/manics/podmanclispawner

WORKDIR /srv/jupyterhub

#RUN touch jupyterhub_cookie_secret
#RUN chmod g+rw jupyterhub_cookie_secret
#RUN openssl rand -hex 32 > jupyterhub_cookie_secret
#RUN chmod 600 jupyterhub_cookie_secret

RUN jupyterhub --generate-config

COPY . .
EXPOSE 8000
CMD . /srv/jupyterhub/env/bin/activate && exec jupyterhub
