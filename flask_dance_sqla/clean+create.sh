podman pod stop frontend
podman pod rm frontend
podman rmi -a
cd /home/andrew_gaitskell/project/flask-mariadb-nginx/flask_dance_sqla
podman build -t my-flaskdancesqla-1 .
podman run -dt --pod new:frontend -p 5000:5000 localhost/my-flaskdancesqla-1:latest
cd /home/andrew_gaitskell/project/flask-mariadb-nginx/mariadb
podman build -t my-mariadb-1 .
podman run -dt --pod frontend -p 3306 localhost/my-mariadb-1:latest -v /run/mysqld/mysqld.sock:/run/mysqld/mysqld.sock
podman pod start frontend
