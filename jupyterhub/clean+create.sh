podman pod stop frontend
podman pod rm frontend
podman rmi -a
cd /home/andrew_gaitskell/project/flask-mariadb-nginx/jupyterhub
podman build -t my-jupyterhub-1 .
podman run -dt --pod new:frontend -p 8000:8000 localhost/my-jupyterhub-1:latest
podman pod start frontend
