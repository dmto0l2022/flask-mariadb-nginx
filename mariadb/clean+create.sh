podman pod stop frontend
podman pod rm frontend
podman rmi -a
cd /home/andrew_gaitskell/project/flask-mariadb-nginx/mariadb
podman build -t my-mariadb-1 .
podman run -dt --pod new:frontend -p 8080:3303  -v /etc/letsencrypt:/etc/letsencrypt localhost/my-mariadb-1:latest
podman pod start frontend
