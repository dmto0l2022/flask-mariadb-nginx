podman pod stop pod-app-backend
podman pod rm pod-app-backend

podman pod create \
--name pod-app-backend \
--infra-name infra-app-backend \
--network bridge \
--publish 5000:5000
##--publish 8080:80

# podman pod create \
# --name pod-data-backend \
# --infra-name infra-data-backend \
# --network bridge \
# --publish 3306:3306

cd /opt/dmtools/code/flask-mariadb-nginx/flask_database
podman build -t my-flaskdatabase-1 .

##cd /opt/dmtools/code/flask-mariadb-nginx/nginx
##podman build -t my-nginx-1 .

# cd /opt/dmtools/code/flask-mariadb-nginx/mariadb
# podman build -t my-mariadb-1 .

##podman run -dt \
##--name nginx_backend-1 \
##--pod pod-app-backend \
##localhost/my-nginx-1:latest

# podman run -dt \
# --name mariadb_backend-1 \
# --pod pod-data-backend \
# localhost/my-mariadb-1:latest

podman run -dt \
--name flaskapp_backend-1 \
--pod pod-app-backend \
localhost/my-flaskdatabase-1:latest

cd /opt/dmtools/code/flask-mariadb-nginx/flask_database
