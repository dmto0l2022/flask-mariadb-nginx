FROM nginx:latest
COPY default.conf /etc/nginx/conf.d/default.conf
COPY dmtools.info.conf /etc/nginx/conf.d/dmtools.info.conf
COPY index.html /usr/share/nginx/html/index.html



VOLUME:
  /etc/letsencrypt/live/dev1.dmtools.info/fullchain.pem
  /etc/letsencrypt/live/dev1.dmtools.info/privkey.pem


