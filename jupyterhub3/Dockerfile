FROM python:3.8
RUN pip3 install \
    'jupyterhub==1.3.*' \
    'notebook==6.*'

ARG USERNAME=agaitske
ARG USER_UID=1001
ARG USER_GID=1002 ## dm group

# create a user, since we don't want to run as root
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN echo "agaitske:agaitske" | chpasswd

ENV HOME=/home/agaitske
WORKDIR $HOME
USER agaitske

RUN export JUPYTERHUB_API_TOKEN=123456789012345678901234567890

CMD ["jupyterhub-singleuser"]
