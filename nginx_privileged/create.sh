podman pod stop frontend
podman pod rm frontend
podman rmi -a
cd /opt/dmtools/code/flask-mariadb-nginx/nginx_privileged
podman build -t my-nginx_priv-1 .
podman run -detach --pod new:frontend -p 8080:80 localhost/my-nginx_priv-1:latest


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
