podman pod stop frontend
podman pod rm frontend
cd /opt/dmtools/code/flask-mariadb-nginx/nginx_githubauth
podman build -t my-nginx-1 .
podman run -dt --pod new:frontend -p 8080:80 localhost/my-nginx-1:latest
#podman run -dt --pod new:frontend -p 443:443 -v /etc/letsencrypt:/etc/letsencrypt localhost/my-nginx-1:latest
podman pod start frontend
