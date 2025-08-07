#!/bin/sh

sed -i "s#__BACKEND_HOST__#$BACKEND_HOST#g" /etc/nginx/nginx.conf
sed -i "s#__BACKEND_PORT__#$BACKEND_PORT#g" /etc/nginx/nginx.conf

exec nginx -g 'daemon off;'     # Default CMD for Nginx Container
