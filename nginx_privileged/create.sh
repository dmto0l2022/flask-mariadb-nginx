podman pod stop pod-frontend
podman pod rm pod-frontend
podman rmi -a

#podman pod create \
#--name pod-frontend \
#--infra-name infra-frontend \
#--publish 8080:80

cd /opt/dmtools/code/flask-mariadb-nginx/nginx_privileged

podman build -t my-nginx_priv-1 .

podman run -detach \
--name nginx_priv-1 \
--publish 8080:80 \
--network bridge \
localhost/my-nginx_priv-1:latest


#podman run --detach \
#--pod frontend \
#--restart=always \
#-e MARIADB_ROOT_PASSWORD="pythonuser" \
#-e MARIADB_DATABASE="world" \
#-e MARIADB_USER="pythonuser" \
#-e MARIADB_PASSWORD="pythonuser" \
#-e MARIADB_ROOT_HOST="localhost" \
#--name=mariadb1 \
# mariadb
