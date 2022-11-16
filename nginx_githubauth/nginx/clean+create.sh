podman pod stop nginx-frontend
podman pod rm nginx-frontend
cd /opt/dmtools/code/flask-mariadb-nginx/nginx_githubauth/nginx
podman build -t my-nginx-1 .
#podman run -dt --pod new:nginx-frontend -p 8080:80 localhost/my-nginx-1:latest
podman run -dt --pod new:nginx-frontend --network=bridge -p 80:80 localhost/my-nginx-1:latest
## you can add 'net.ipv4.ip_unprivileged_port_start=80' to /etc/sysctl.conf (currently 1024)
#podman run -dt --pod new:frontend -p 443:443 -v /etc/letsencrypt:/etc/letsencrypt localhost/my-nginx-1:latest

