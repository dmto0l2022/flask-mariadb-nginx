podman pod stop pod-backend
podman pod rm pod-backend

podman pod create \
--name pod-backend \
--infra \
--infra-name infra-backend \
--publish 5000:5000 \
--network bridge

cd /opt/dmtools/code/flask-mariadb-nginx/flask_nopath

podman build -t my-flask-1 .

podman run -detach \
--name flask-1 \
--pod pod-backend \
--network bridge \
localhost/my-flask-1:latest

cd /opt/dmtools/code/flask-mariadb-nginx/nginx_privileged
