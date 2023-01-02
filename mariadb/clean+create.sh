podman pod stop pod_mariadb_backend
podman pod rm pod_mariadb_backend
cd /opt/dmtools/code/flask-mariadb-nginx/mariadb

uid=1001
gid=1002
subuidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.UIDMap }}+{{.Size }}{{end }}" ) - 1 ))
subgidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.GIDMap }}+{{.Size }}{{end }}" ) - 1 ))

podman pod create \
--name pod_mariadb_backend \
--infra-name infra_mariadb_backend \
--network bridge \
--uidmap 0:1:$uid \
--uidmap $uid:0:1 \
--uidmap $(($uid+1)):$(($uid+1)):$(($subuidSize-$uid)) \
--gidmap 0:1:$gid \
--gidmap $gid:0:1 \
--gidmap $(($gid+1)):$(($gid+1)):$(($subgidSize-$gid)) \
--publish 3306:3306

podman build -t my_mariadb_1 .

##-v /HOST-DIR:/CONTAINER-DIR

podman run -dt \
--name mariadb_backend_1 \
--pod pod_mariadb_backend \
--volume /opt/dmtools/mysql:/var/lib/mysql:z \
--user $uid:$gid \
localhost/my_mariadb_1:latest
