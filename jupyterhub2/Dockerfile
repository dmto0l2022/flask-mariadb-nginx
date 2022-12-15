FROM python:3
RUN apt-get update && apt-get -y update \
    && apt-get -y install npm python3-venv

#RUN mkdir /docker-entrypoint-initdb.d ## already exists
#RUN chown $USER_UID:$USER_GID /docker-entrypoint-initdb.d
#RUN chown $USER_UID:$USER_GID /var/lib/mysql

#################
WORKDIR /workdir

ARG USERNAME=agaitske
ARG USER_UID=1001
ARG USER_GID=1002 ## dm group

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

#RUN mkdir /docker-entrypoint-initdb.d ## already exists
#RUN chown $USER_UID:$USER_GID /docker-entrypoint-initdb.d
#RUN chown $USER_UID:$USER_GID /var/lib/mysql
RUN chown $USER_UID:$USER_GID /workdir

RUN mkdir /workdir/uploads
RUN chown $USER_UID:$USER_GID /workdir/uploads

USER $USERNAME

## https://pythonspeed.com/articles/activate-virtualenv-dockerfile/

ENV VIRTUAL_ENV=/workdir/app/env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
##COPY requirements.txt .
##RUN pip install -r requirements.txt

# Run the application:
#COPY myapp.py .
#CMD ["python", "myapp.py"]


##RUN python3 -m venv /app/env
##RUN /app/env/bin/python -m pip install --upgrade pip
RUN /workdir/app/env/bin/python3 -m pip install --upgrade pip
RUN . /workdir/app/env/bin/activate
RUN /workdir/app/env/bin/python3 --version
RUN whereis python3
RUN whereis pip3
COPY requirements.txt /workdir/requirements.txt
RUN /workdir/app/env/bin/pip3 install -r /workdir/requirements.txt
RUN /workdir/app/env/bin/pip3 freeze
COPY . /workdir/.
##RUN ls -R /workdir/
EXPOSE 8002
##CMD [ "/app/env/bin/python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8002"]
##RUN chmod +x //app/entry-point.sh
ENTRYPOINT ["sh","/workdir/entry-point.sh"]

################


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

