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

CMD ["jupyterhub-singleuser" "-f /home/agaitske/jupyterhub_config.py"]
