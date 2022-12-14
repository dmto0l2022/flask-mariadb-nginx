uid=1001
gid=1002
subuidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.UIDMap }}+{{.Size }}{{end }}" ) - 1 ))
subgidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.GIDMap }}+{{.Size }}{{end }}" ) - 1 ))

podman network create jupyter_network

podman pod create \
--name pod-jupyterhub \
--infra-name infra-jupyter-frontend \
--network jupyter_network \
--uidmap 0:1:$uid \
--uidmap $uid:0:1 \
--uidmap $(($uid+1)):$(($uid+1)):$(($subuidSize-$uid)) \
--gidmap 0:1:$gid \
--gidmap $gid:0:1 \
--gidmap $(($gid+1)):$(($gid+1)):$(($subgidSize-$gid)) \
--publish 8000:8000 --publish 8001:8001 --publish 8002:8002

podman build -t my-jupyterhub-1 .

##-v /HOST-DIR:/CONTAINER-DIR

podman run -dt \
--name jupyterhub \
--pod pod-jupyterhub \
--volume /opt/dmtools/notebooks:/workdir/notebooks:z \
--volume /opt/dmtools/jupyterhub:/workdir/jupyterhub:z \
--user $uid:$gid \
localhost/my-jupyterhub-1:latest
