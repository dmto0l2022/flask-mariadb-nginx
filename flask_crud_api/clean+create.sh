podman pod stop pod-api-backend
podman pod rm pod-api-backend
cd /opt/dmtools/code/flask-mariadb-nginx/flask_crud_api

uid=1001
gid=1002
subuidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.UIDMap }}+{{.Size }}{{end }}" ) - 1 ))
subgidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.GIDMap }}+{{.Size }}{{end }}" ) - 1 ))

podman pod create \
--name pod-api-backend \
--infra-name infra-api-backend \
--network bridge \
--uidmap 0:1:$uid \
--uidmap $uid:0:1 \
--uidmap $(($uid+1)):$(($uid+1)):$(($subuidSize-$uid)) \
--gidmap 0:1:$gid \
--gidmap $gid:0:1 \
--gidmap $(($gid+1)):$(($gid+1)):$(($subgidSize-$gid)) \
--publish 8004:8004

podman build -f Dockerfile_pythonbase -t my-pythonbaseapi-1 .
podman build -f Dockerfile_pythonapi -t my-pythonapi-1 .

##-v /HOST-DIR:/CONTAINER-DIR

podman run -dt \
--name api_backend-1 \
--pod pod-api-backend \
--user $uid:$gid \
localhost/my-pythonapi-1:latest
