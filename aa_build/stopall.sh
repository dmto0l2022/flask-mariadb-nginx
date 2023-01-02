podman stop api_backend_1
podman stop infra_api_backend

podman pod stop pod_api_backend
podman pod rm pod_api_backend


#CONTAINER ID  IMAGE                                    COMMAND               CREATED        STATUS             PORTS                   NAMES
#6c569b6a2198  localhost/podman-pause:4.2.0-1666812227                        8 minutes ago  Up 8 minutes ago   0.0.0.0:3306->3306/tcp  infra-db-backend
#f6e75b86d41c  localhost/my-mariadb-1:latest            mysqld                8 minutes ago  Up 8 minutes ago   0.0.0.0:3306->3306/tcp  db_backend-1
#5bc3174c2b0a  localhost/podman-pause:4.2.0-1666812227                        8 minutes ago  Up 3 minutes ago   0.0.0.0:8004->8004/tcp  infra_api_backend
#2e06f4cf9c13  localhost/my_pythonapi_1:latest          gunicorn --bind 0...  5 minutes ago  Up 3 minutes ago   0.0.0.0:8004->8004/tcp  api_backend_1
#177ef2a893ae  localhost/podman-pause:4.2.0-1666812227                        3 minutes ago  Up 28 seconds ago  0.0.0.0:8002->8002/tcp  infra_flask_dash_frontend
#2ffffb730aef  localhost/flask_dash_frontend_1:latest   gunicorn --bind 0...  2 minutes ago  Up 28 seconds ago  0.0.0.0:8002->8002/tcp  flask_dash_frontend_1
