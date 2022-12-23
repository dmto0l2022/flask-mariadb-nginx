podman pod stop pod-python-frontend
podman pod rm pod-python-frontend
cd /opt/dmtools/code/flask-mariadb-nginx/flask_dash_frontend

uid=1001
gid=1002
subuidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.UIDMap }}+{{.Size }}{{end }}" ) - 1 ))
subgidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.GIDMap }}+{{.Size }}{{end }}" ) - 1 ))

podman pod create \
--name pod-python-frontend \
--infra-name infra-python-frontend \
--network bridge \
--uidmap 0:1:$uid \
--uidmap $uid:0:1 \
--uidmap $(($uid+1)):$(($uid+1)):$(($subuidSize-$uid)) \
--gidmap 0:1:$gid \
--gidmap $gid:0:1 \
--gidmap $(($gid+1)):$(($gid+1)):$(($subgidSize-$gid)) \
--publish 8002:8002

#podman build -f Dockerfile_pythonbase -t my-pythonbaseapi-1 .
podman build -f Dockerfile_pythonfrontend -t my-pythonfrontend-1 .

##-v /HOST-DIR:/CONTAINER-DIR

podman run -dt \
--name python_frontend-1 \
--pod pod-python_frontend-1 \
--user $uid:$gid \
localhost/my-pythonfrontend-1:latest
