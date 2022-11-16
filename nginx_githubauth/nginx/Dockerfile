FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /var/www
RUN mkdir /var/www/html

#COPY nginx.conf /etc/nginx/conf.d
#COPY simple80.conf /etc/nginx/conf.d
COPY locs.conf /etc/nginx/conf.d
COPY index1.html /var/www/html/index.html

#COPY server_default.conf /etc/nginx/conf.d/default.conf
#COPY default.conf /etc/nginx/conf.d/default.conf
#COPY dmtools.info.conf /etc/nginx/conf.d/dmtools.info.conf
#COPY index.html /usr/share/nginx/html/index.html

#RUN mkdir -p /etc/letsencrypt/live/dev1.dmtools.info
#COPY fullchain.pem /etc/letsencrypt/live/dev1.dmtools.info/fullchain.pem
#COPY privkey.pem /etc/letsencrypt/live/dev1.dmtools.info/privkey.pem
#COPY options-ssl-nginx.conf /etc/letsencrypt/options-ssl-nginx.conf

#VOLUME:
#  /etc/letsencrypt/live/dev1.dmtools.info/fullchain.pem
#  /etc/letsencrypt/live/dev1.dmtools.info/privkey.pem
