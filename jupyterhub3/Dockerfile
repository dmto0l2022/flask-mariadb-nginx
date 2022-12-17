FROM python:3.10
RUN pip3 install \
    'jupyterhub' \
    'notebook'

ARG USERNAME=agaitske
ARG USER_UID=1001
ARG USER_GID=1002 ## dm group

ADD jupyterhub_config.py /home/agaitske/jupyterhub_config.py

# create a user, since we don't want to run as root
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN echo "agaitske:agaitske" | chpasswd

ENV HOME=/home/agaitske
WORKDIR $HOME
USER agaitske

# these must match the values in jupyterhub_config.py
export JUPYTERHUB_API_TOKEN=8b1b11907e4511eda1eb0242ac120002
export JUPYTERHUB_SERVICE_URL=http://127.0.0.1:9999
export JUPYTERHUB_SERVICE_NAME=shared-notebook
export JUPYTERHUB_SERVICE_PREFIX="/services/${JUPYTERHUB_SERVICE_NAME}/"
export JUPYTERHUB_CLIENT_ID="service-${JUPYTERHUB_SERVICE_NAME}"

CMD ["jupyterhub-singleuser" "-f /home/agaitske/jupyterhub_config.py"]
