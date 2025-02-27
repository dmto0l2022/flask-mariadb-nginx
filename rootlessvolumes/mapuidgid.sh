uid=1001
gid=1002
subuidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.UIDMap }}+{{.Size }}{{end }}" ) - 1 ))
subgidSize=$(( $(podman info --format "{{ range \
   .Host.IDMappings.GIDMap }}+{{.Size }}{{end }}" ) - 1 ))
podman run --rm \
  --user $uid:$gid \
  --uidmap 0:1:$uid \
  --uidmap $uid:0:1 \
  --uidmap $(($uid+1)):$(($uid+1)):$(($subuidSize-$uid)) \
  --gidmap 0:1:$gid \
  --gidmap $gid:0:1 \
  --gidmap $(($gid+1)):$(($gid+1)):$(($subgidSize-$gid)) \
     docker.io/library/ubuntu /bin/cat /proc/self/uid_map
     
     
podman run -dit --volume /src:/dest:z \
  --user $uid:$gid \
  --uidmap 0:1:$uid \
  --uidmap $uid:0:1 \
  --uidmap $(($uid+1)):$(($uid+1)):$(($subuidSize-$uid)) \
  --gidmap 0:1:$gid \
  --gidmap $gid:0:1 \
  --gidmap $(($gid+1)):$(($gid+1)):$(($subgidSize-$gid)) \
 --name busybox busybox
 
 
 podman run -dit --volume /opt/dmtools/mysql:/dest:z \
  --user $uid:$gid \
  --uidmap 0:1:$uid \
  --uidmap $uid:0:1 \
  --uidmap $(($uid+1)):$(($uid+1)):$(($subuidSize-$uid)) \
  --gidmap 0:1:$gid \
  --gidmap $gid:0:1 \
  --gidmap $(($gid+1)):$(($gid+1)):$(($subgidSize-$gid)) \
 --name busybox1 busybox
     
