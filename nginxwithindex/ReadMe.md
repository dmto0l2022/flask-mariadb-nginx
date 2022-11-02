# Introduction

This shows how to create a flask app using podman with an index page

# test with simple hello world flask app

## empty podman world

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

# test with nginx & flask app

## change in to app folder

cd /flask-mariadb-nginx/flask

## create image from Dockefile

podman build -t my-flask-1 .

cd ..

cd nginxwithindex

podman build -t my-nginxwithindex-1 .

## create pod

podman run -dt --pod new:frontend -p 8080:80 localhost/my-nginxwithindex-1:latest

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
