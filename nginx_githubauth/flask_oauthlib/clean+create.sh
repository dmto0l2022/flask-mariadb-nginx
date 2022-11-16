podman pod stop flask-frontend
podman pod rm flask-frontend
podman build -t my-flask5000-1 .
podman run -dt --pod new:flask-frontend --name=flaskpod --network=bridge -p 5000:5000 localhost/my-flask5000-1:latest

