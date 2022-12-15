FROM python:3
RUN apt-get update && apt-get -y update \
    && apt-get -y install npm python3-venv

ARG USERNAME=agaitske
ARG USER_UID=1001
ARG USER_GID=1002 ## dm group

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

#RUN mkdir /docker-entrypoint-initdb.d ## already exists
#RUN chown $USER_UID:$USER_GID /docker-entrypoint-initdb.d
#RUN chown $USER_UID:$USER_GID /var/lib/mysql

USER $USERNAME
#RUN $HOME
RUN mkdir "${HOME}/.npm-packages"
RUN npm config set prefix "${HOME}/.npm-packages"
RUN export PATH="$PATH:${HOME}/.npm-packages/bin"
RUN npm install -g configurable-http-proxy

RUN python3 -mvenv $HOME/jhenv

RUN $HOME/jhenv/bin/pip install jupyterhub dockerspawner

COPY jupyterhub_config.py jupyterhub_config.py

CMD . $HOME/jhenv/bin/activate & exec jupyterhub --debug --config=jupyterhub_config.py

