FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /var/www
RUN mkdir /var/www/html

COPY nginx_starter.conf /etc/nginx/conf.d
COPY index.html /var/www/html
