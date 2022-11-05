podman pod stop frontend
podman pod rm frontend
podman rmi $(podman images -qa) -f

## docker run -p 3306:3306 -d --name mariadb -e MARIADB_ROOT_PASSWORD=Password123! mariadb/server:10.4 
## podman run -dt --pod new:frontend -p 3306:3306 localhost/my-mariadb-1:latest

podman pod create \
--name frontend \
--publish 5000:5000

#env MARIADB_USER=pythonuser
#env MARIADB_PASSWORD=pythonuser
#env MARIADB_ROOT_PASSWORD=pythonuser
#env MARIADB_DATABASE=world

#podman run --detach \
#--pod frontend \
#--restart=always \
#-e MARIADB_ROOT_PASSWORD="pythonuser" \
#-e MARIADB_DATABASE="world" \
#-e MARIADB_USER="pythonuser" \
#-e MARIADB_PASSWORD="pythonuser" \
#-e MARIADB_ROOT_HOST="localhost" \
#--name=mariadb1 mariadb

##podman run -dt --pod new:frontend -p 3306:3306 -e MARIADB_ROOT_PASSWORD=Password123! mariadb/server:10.4

cd /home/andrew_gaitskell/project/flask-mariadb-nginx/mariadb
podman build -t my-mariadb-1:latest .
podman run -dt \
--pod frontend \
--name=mariadb1 \
localhost/my-mariadb-1:latest

cd /home/andrew_gaitskell/project/flask-mariadb-nginx/flask_dance_sqla
podman build -t my-flaskdancesqla-1 .

podman run -dt \
--pod frontend \
localhost/my-flaskdancesqla-1:latest

podman pod start frontend
