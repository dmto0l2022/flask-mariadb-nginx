podman pod stop backend
podman pod rm backend

podman pod create \
--name backend \
--publish 5000:5000

cd /opt/dmtools/code/flask-mariadb-nginx/flask_nopath

podman build -t my-flask-1 .

podman run -detach \
--pod backend \
--name=flask-1 \
localhost/my-flask-1:latest

cd /opt/dmtools/code/flask-mariadb-nginx/nginx_privileged
