podman pod stop db-frontend
podman pod rm db-frontend
podman rmi -a
cd /opt/dmtools/code/flask-mariadb-nginx/mariadb
podman build -t my-mariadb-1 .
podman run -dt --pod new:db-frontend -p 3306:3306 localhost/my-mariadb-1:latest
podman pod start db-frontend
