FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /var/www
RUN mkdir /var/www/html

COPY /config/nginx.conf /etc/nginx/conf.d
COPY index.html /var/www/html
