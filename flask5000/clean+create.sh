podman pod stop frontend
podman pod rm frontend
podman rmi -a
podman build -t my-flask5000-1 .
podman run -dt --pod new:frontend --network=host -p 5000 localhost/my-flask5000-1:latest
podman pod start frontend
