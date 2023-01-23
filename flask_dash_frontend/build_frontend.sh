uid=${ENV_UID} ##1001
gid=${ENV_GID} ##1002

subuidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.UIDMap }}+{{.Size }}{{end }}" ) - 1 ))
subgidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.GIDMap }}+{{.Size }}{{end }}" ) - 1 ))

#podman build -f Dockerfile_pythonfrontendbase -t image_python_base_frontend_1 .
podman rmi flask_dash_frontend_1:latest
podman build -f Dockerfile_pythonfrontend -t flask_dash_frontend_1 .

##-v /HOST-DIR:/CONTAINER-DIR

## podman pull docker.io/dmto0l2022/flask_dash_frontend_1:latest

podman run -dt \
--name container_flask_dash_frontend_1 \
--pod pod_main_backend \
--user $uid:$gid \
localhost/flask_dash_frontend_1:latest
