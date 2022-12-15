podman pull registry.redhat.io/rhel8/httpd-24
podman create --name httpd -p 127.0.0.1:8080:8080 \
-v ~/www-data:/var/www/html/:Z \
registry.redhat.io/rhel8/httpd-24
