podman pod stop frontend
podman pod rm frontend
podman rmi -a
cd /home/andrew_gaitskell/project/flask-mariadb-nginx/nginx_https
podman build -t my-nginx-1 .
podman run -dt --pod new:frontend -p 8080:80 -v /etc/letsencrypt:/etc/letsencrypt localhost/my-nginx-1:latest
podman pod start frontend
