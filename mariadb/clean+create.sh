podman pod stop pod-db-backend
podman pod rm pod-db-backend
cd /opt/dmtools/code/flask-mariadb-nginx/mariadb

podman pod create \
--name pod-db-backend \
--infra-name infra-db-backend \
--network bridge \
--publish 3306:3306

podman build -t my-mariadb-1 .

##-v /HOST-DIR:/CONTAINER-DIR

podman run -dt \
--name db_backend-1 \
--pod pod-db-backend \
--user 1001 \
--volume /opt/dmtools/mysql:/var/lib/mysql \
localhost/my-mariadb-1:latest
