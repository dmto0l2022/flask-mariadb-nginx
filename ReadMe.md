# B4 flask-security-too changes


# Introduction

This shows how to create a flask app using podman

# generate model files from existing database

    https://pypi.org/project/sqlacodegen/

# test with flask app

## empty podman world

### list all podman processes

    lsns

### major reset

    podman system reset

### stop pod

    podman pod stop frontend

### remove pod

    podman pod rm frontend

### list all images

    podman images

### remove all images

    podman rmi -a

## list all containers

    podman ps -a

# Introduction

This shows how to create a flask app behind nginx using podman

# test with nginx & django app

## change in to app folder

cd /flask-mariadb-nginx/flask

## create image from Dockefile

podman build -t my-flask-1 .

cd ..

cd nginx

podman build -t my-nginx-1 .

## create pod

podman run -dt --pod new:frontend -p 8080:80 localhost/my-nginx-1:latest

## add image to pod

podman run -dt --pod frontend localhost/my-flask-1:latest


## start pod

podman pod start frontend

## visit

http://35.214.57.82:8080/

## stop pod

podman pod stop frontend

## remove pod

podman pod rm frontend

## list all images

podman images

## remove all images

podman rmi -a

podman -rmi image-id

## list all containers

podman ps -a
