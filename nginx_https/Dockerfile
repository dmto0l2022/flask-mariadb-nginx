FROM nginx:latest
COPY default.conf /etc/nginx/conf.d/default.conf
COPY dev1.dmtools.info.conf /etc/nginx/conf.d/dmtools.info.conf

VOLUME:
  /etc/letsencrypt/live/dev1.dmtools.info/fullchain.pem
  /etc/letsencrypt/live/dev1.dmtools.info/privkey.pem


