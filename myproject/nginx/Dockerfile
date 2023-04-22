FROM nginx:stable

WORKDIR /var/www/server

RUN mkdir /var/www/server/staticfiles

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

EXPOSE 80
