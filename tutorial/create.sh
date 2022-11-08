#!/bin/bash
# create_blog.sh

set -e   #exit on most errors

podman pod create --name blog --infra --publish 8080:80 --network bridge 

podman run --pod blog --name mysql -e MYSQL_USER=alexon \
-e MYSQL_PASSWORD=123456 -e MYSQL_DATABASE=wpdb \
-e MYSQL_ROOT_PASSWORD=567890 \
--volume /var/local/mysql:/var/lib/mysql:Z \
-d docker.io/library/mysql 

podman run --pod blog --name wordpress -e WORDPRESS_DB_HOST=mysql \
-e WORDPRESS_DB_USER=alexon \
-e WORDPRESS_DB_PASSWORD=123456 \
-e WORDPRESS_DB_NAME=wpdb \
-d docker.io/library/wordpress

