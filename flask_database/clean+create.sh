podman pod stop pod-backend
podman pod rm pod-backend
podman rmi -a


podman pod create \
--name pod-backend \
--infra-name infra-backend \
--network bridge \
--publish 8080:80

podman pod create \
--name pod-database \
--infra-name infra-backend \
--network bridge \
--publish 3306:3306

cd /opt/dmtools/code/flask-mariadb-nginx/flask_database
podman build -t my-flaskdatabase-1 .
cd /opt/dmtools/code/flask-mariadb-nginx/nginx
podman build -t my-nginx-1 .
cd /opt/dmtools/code/flask-mariadb-nginx/mariadb
podman build -t my-mariadb-1 .

podman run -dt \
--name nginx_backend-1 \
--pod pod-backend \
localhost/my-nginx-1:latest

podman run -dt \
--name mariadb_backend-1 \
--pod pod-database \
localhost/my-mariadb-1:latest

podman run -dt \
--name flaskapp_backend-1 \
--pod pod-backend \
localhost/my-flaskdatabase-1:latest

cd /opt/dmtools/code/flask-mariadb-nginx/flask_database
