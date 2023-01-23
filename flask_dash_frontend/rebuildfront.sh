podman stop container_flask_dash_frontend_1
podman rm container_flask_dash_frontend_1
podman rmi image_flask_dash_frontend_1

podman build -f Dockerfile_pythonfrontend -t image_flask_dash_frontend_1 .

##-v /HOST-DIR:/CONTAINER-DIR

podman run -dt \
--name container_flask_dash_frontend_1 \
--pod pod_flask_dash_frontend \
--user $uid:$gid \
localhost/image_flask_dash_frontend_1:latest

