cd /opt/dmtools/code/flask-mariadb-nginx/redis
podman rmi redis_1
podman build -f Dockerfile -t redis_1 .
podman tag image_redis_1:latest dmto0l2022/redis_1:latest
podman push docker.io/dmto0l2022/redis_1:latest

cd /opt/dmtools/code/flask-mariadb-nginx/mariadb
podman rmi mariadb_1

podman build \
--build-arg=ENV_UID=${ENV_UID} \
--build-arg=ENV_USERNAME=${ENV_USERNAME} \
--build-arg=ENV_GID=${ENV_GID} \
--build-arg=ENV_GROUPNAME=${ENV_GROUPNAME} \
--build-arg=ENV_MARIADB_USER=${ENV_MARIADB_USER} \
--build-arg=ENV_MARIADB_PASSWORD=${ENV_MARIADB_PASSWORD} \
--build-arg=ENV_MARIADB_ROOT_PASSWORD=${ENV_MARIADB_ROOT_PASSWORD} \
--build-arg=ENV_MARIADB_DATABASE=${ENV_MARIADB_DATABASE} \
-t mariadb_1 .

## not pushing the above for obvious reasons!

podman stop container_api_backend_1
podman rmi pythonbaseapi_1
podman rmi pythonapi_1
cd /opt/dmtools/code/flask-mariadb-nginx/flask_crud_api

podman build -f Dockerfile_pythonbase -t pythonbaseapi_1 .
podman tag pythonbaseapi_1:latest dmto0l2022/pythonbaseapi_1:latest
podman push docker.io/dmto0l2022/pythonbaseapi_1:latest

podman build -f Dockerfile_pythonapi -t pythonapi_1 .
podman tag pythonapi_1:latest dmto0l2022/pythonapi_1:latest
podman push docker.io/dmto0l2022/pythonapi_1:latest

podman stop container_flask_dash_frontend_1
podman rmi python_base_frontend_1
podman rmi flask_dash_frontend_1

cd /opt/dmtools/code/flask-mariadb-nginx/flask_dash_frontend

podman build -f Dockerfile_pythonfrontendbase -t python_base_frontend_1 .
podman tag python_base_frontend_1:latest dmto0l2022/python_base_frontend_1:latest
podman push docker.io/dmto0l2022/python_base_frontend_1:latest

podman build -f Dockerfile_pythonfrontend -t flask_dash_frontend_1 .
podman tag flask_dash_frontend_1:latest dmto0l2022/flask_dash_frontend_1:latest
podman push docker.io/dmto0l2022/flask_dash_frontend_1:latest

