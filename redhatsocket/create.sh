
podman pull registry.redhat.io/rhel8/httpd-24

podman create --name httpd -p 0.0.0.0:8000:8000 \
-v /opt/dmtools/code/flask-mariadb-nginx/redhatsocket/www-data:/var/www/html/:Z \
registry.redhat.io/rhel8/httpd-24
