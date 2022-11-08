podman pod stop frontend
podman pod rm frontend
podman rmi -a
cd /opt/dmtools/code/flask-mariadb-nginx/flask_database
podman build -t my-flaskdatabase-1 .
cd /opt/dmtools/code/flask-mariadb-nginx/nginx
podman build -t my-nginx-1 .
podman run -dt --pod new:frontend -p 8080:80 localhost/my-nginx-1:latest
podman run -dt --pod frontend localhost/my-flaskdatabase-1:latest
podman pod start frontend
