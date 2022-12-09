podman pod stop pod-db-backend
podman pod rm pod-db-backend
cd /opt/dmtools/code/flask-mariadb-nginx/mariadb

uid=1001
gid=1002
subuidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.UIDMap }}+{{.Size }}{{end }}" ) - 1 ))
subgidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.GIDMap }}+{{.Size }}{{end }}" ) - 1 ))

podman pod create \
--name pod-db-backend \
--infra-name infra-db-backend \
--network bridge \
--uidmap 0:1:$uid \
--uidmap $uid:0:1 \
--uidmap $(($uid+1)):$(($uid+1)):$(($subuidSize-$uid)) \
--gidmap 0:1:$gid \
--gidmap $gid:0:1 \
--gidmap $(($gid+1)):$(($gid+1)):$(($subgidSize-$gid)) \
--publish 3306:3306

podman build -t my-mariadb-1 .

##-v /HOST-DIR:/CONTAINER-DIR

podman run -dt \
--name db_backend-1 \
--pod pod-db-backend \
--volume /opt/dmtools/mysql:/var/lib/mysql:z \
--user $uid:$gid \
localhost/my-mariadb-1:latest
