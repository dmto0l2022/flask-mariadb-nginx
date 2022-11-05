podman pod stop frontend
podman pod rm frontend
podman rmi -a
 
podman run -p 3306:3306 -d --name mariadb -e MARIADB_ROOT_PASSWORD=Password123! mariadb/server:10.4
 
