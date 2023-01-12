podman stop container_1
podman stop container_2

podman pod rm pod_main
podman rmi nginx:latest

podman pod create \
--name pod_main \
--infra-name infra_1 \
--network bridge \
--publish 80:80

podman build -f Dockerfile8080 -t image_nginx8080 .
podman build -f Dockerfile8090 -t image_nginx8090 .

##-v /HOST-DIR:/CONTAINER-DIR

podman run -dt \
--name container_1 \
--pod pod_main \
localhost/image_nginx8080:latest

podman run -dt \
--name container_2 \
--pod pod_main \
localhost/image_nginx8090:latest

