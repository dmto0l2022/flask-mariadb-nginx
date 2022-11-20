podman pod stop jupyter-frontend
podman pod rm jupyter-frontend
cd /opt/dmtools/code/flask-mariadb-nginx/jupyterhub
podman build -t my-jupyterhub-1 .
podman run -dt --pod new:jupyter-frontend -p 8000:8000 -p 8001:8001 -p 8002:8002 localhost/my-jupyterhub-1:latest
podman pod start jupyter-frontend
