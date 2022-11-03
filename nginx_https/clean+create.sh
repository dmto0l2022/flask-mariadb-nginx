podman pod stop frontend
podman pod rm frontend
podman rmi -a
cd /home/andrew_gaitskell/project/flask-mariadb-nginx/nginx_https
podman build -t my-nginx-1 .
podman run -dt --pod new:frontend -p 8080:80 localhost/my-nginx-1:latest

podman run -d -p 8080:8000 --name webapp1 -v /opt/data:/opt oraclelinux:pyhttp


podman pod start frontend
