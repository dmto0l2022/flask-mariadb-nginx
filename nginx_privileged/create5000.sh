cd /opt/dmtools/code/flask-mariadb-nginx/flask_nopath
podman build -t my-flask-1 .
podman run -dt --pod new:backend -p 5000 localhost/my-flask-1:latest
podman pod start backend


cd /opt/dmtools/code/flask-mariadb-nginx/nginx_privileged
