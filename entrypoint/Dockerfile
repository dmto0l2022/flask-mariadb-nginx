FROM python:3.9-alpine

WORKDIR /app
COPY . /app

RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT ['./entrypoint.sh']
