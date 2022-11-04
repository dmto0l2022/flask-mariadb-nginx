podman pod stop frontend
podman pod rm frontend
podman rmi -a
cd /home/andrew_gaitskell/project/flask-mariadb-nginx/flask_dance
podman build -t my-flaskdance-1 .
podman run -dt --pod new:frontend -p 5000:5000 localhost/my-flaskdance-1:latest
cd /home/andrew_gaitskell/project/flask-mariadb-nginx/mariadb
podman build -t my-mariadb-1 .
podman run -dt --pod frontend -p 3306 localhost/my-mariadb-1:latest
podman pod start frontend
