FROM python:3
RUN apt-get update && apt-get -y update \
    && apt-get -y install npm podman python3-venv

#RUN $HOME
RUN mkdir "${HOME}/.npm-packages"
RUN npm config set prefix "${HOME}/.npm-packages"
RUN export PATH="$PATH:${HOME}/.npm-packages/bin"
RUN npm install -g configurable-http-proxy

RUN python3 -mvenv $HOME/jhenv

COPY jupyterhub_config.py jupyterhub_config.py

CMD . $HOME/jhenv/bin/activate & exec jupyterhub --debug --config=jupyterhub_config.py

