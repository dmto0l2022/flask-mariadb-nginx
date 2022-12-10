FROM python:3.8-slim-buster
RUN apt-get update && apt-get -y install vim
RUN apt-get -y install unzip

WORKDIR /app

ARG USERNAME=agaitske
ARG USER_UID=1001
ARG USER_GID=1002 ## dm group

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

#RUN mkdir /docker-entrypoint-initdb.d ## already exists
#RUN chown $USER_UID:$USER_GID /docker-entrypoint-initdb.d
#RUN chown $USER_UID:$USER_GID /var/lib/mysql
RUN chown $USER_UID:$USER_GID /app

USER $USERNAME

RUN python3 -m venv /app/env
RUN . /app/env/bin/activate
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000"]
