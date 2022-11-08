podman pod stop frontend
podman pod rm frontend
podman rmi -a
cd /opt/dmtools/code/flask-mariadb-nginx/nginx_privileged
podman build -t my-nginx_priv-1 .
podman run -dt --pod new:frontend -p 8080:80 localhost/my-nginx_priv-1:latest
