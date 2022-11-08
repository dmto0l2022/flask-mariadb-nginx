podman pod stop pod-backend
podman pod rm pod-backend

podman pod create \
--name pod-backend \
--infra-name infra-backend \
--publish 5000

cd /opt/dmtools/code/flask-mariadb-nginx/flask_nopath

podman build -t my-flask-1 .

podman run -detach \
--pod pod-backend \
--name flask-1 \
localhost/my-flask-1:latest

cd /opt/dmtools/code/flask-mariadb-nginx/nginx_privileged
