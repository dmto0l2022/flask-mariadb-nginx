podman pod stop frontend-nginx
podman pod rm frontend-nginx
cd /opt/dmtools/code/flask-mariadb-nginx/nginxwithindex
podman build -t my-nginxwithindex-1 .
#podman run -dt --pod new:frontend -p 8080:80 localhost/my-nginxwithindex-1:latest
podman run -dt --pod new:frontend -p 80:80 localhost/my-nginxwithindex-1:latest
