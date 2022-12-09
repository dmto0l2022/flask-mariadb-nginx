# Reference & Thanks

https://blog.christophersmart.com/2021/01/31/volumes-and-rootless-podman/

# Experiments

## 1

podman run -dit --volume /opt/dmtools/mysql:/dest busybox

## Host-dir volumes and rootless containers, running as root

OK so this is where things start to get a little more interesting as the uid in the container is NOT the same as our user (and we’re not root on the host) and podman will not help us out here (as it does with container volumes above).

We cannot just create a host directory as our non-root host user and pass it through, as the permissions inside the container will be root.
$ mkdir src
 
$ ls -lZd src
drwxrwxr-x. 2 csmart csmart system_u:object_r:container_file_t:s0 6 Jan 31 19:15 src
 
$ podman run -dit --volume ./src:/dest:z --user 123:123 --name busybox busybox
bd9b8e7685acaa3b03380a10724bd2c06ddaa48dbfb67b49339068e16f51d57c
 
$ podman exec busybox id
uid=123(123) gid=123(123)
 
$ podman exec busybox ls -ld /dest
drwxrwxr-x    2 root     root             6 Jan 31 08:15 /dest
 
$ podman exec busybox touch /dest/file
touch: /dest/file: Permission denied

Obviously the container user is not able to write to the volume. So what do we do? Well we need to change the permissions so that they match the user (similar to what podman does for us automatically when using a container volume).

If you have root on the box, that’s pretty easy.
1
2
3
4
5
6
7
8
9
	
$ chown 100122:100122 src
 
$ ls -lZd src
drwxrwxr-x. 2 100122 100122 system_u:object_r:container_file_t:s0 6 Jan 31 19:15 src
 
$ podman exec busybox touch /dest/file
 
$ ls -lZ src/file
-rw-r--r--. 1 100122 100122 system_u:object_r:container_file_t:s0 0 Jan 31 19:20 src/file

OK, but remember we’re running rootless containers, so how do you do that as your regular old non-root user if you don’t have root on the host?
1
2
	
$ chown 100122:100122 src/
chown: changing ownership of 'src/': Operation not permitted

Remember that podman unshare command (see previous post) which under a new user namespace? We can use this to set the permissions, but remember we don’t actually set it to 100122 as it will be on the host, we use the container uid of 123:123.
$ podman unshare chown 123:123 ./src
 
$ ls -lZd src
drwxrwxr-x. 2 100122 100122 system_u:object_r:container_file_t:s0 18 Jan 31 19:20 src

Now the host directory has the right permissions and the container user will be able to write just fine!
1
2
3
4
	
$ podman exec busybox touch /dest/file
 
$ ls -lZ src/file
-rw-r--r--. 1 100122 100122 system_u:object_r:container_file_t:s0 0 Jan 31 19:23 src/file
Accessing data as non-root user and non-
