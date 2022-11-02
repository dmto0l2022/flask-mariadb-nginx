podman pod stop frontend
podman pod rm frontend
podman rmi -a
cd /home/andrew_gaitskell/project/flask-mariadb-nginx/flask_nopath
podman build -t my-flask-1 .
cd /home/andrew_gaitskell/project/flask-mariadb-nginx/nginxwithindex
podman build -t my-nginxwithindex-1 .
podman run -dt --pod new:frontend -p 8080:80 localhost/my-nginxwithindex-1:latest
podman run -dt --pod frontend localhost/my-flask-1:latest
podman pod start frontend
