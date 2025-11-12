FROM nginx:alpine

ENV FRONTEND_PORT=8080
ENV BACKEND_HOST=127.0.0.1
ENV BACKEND_PORT=5000

RUN rm -rf /usr/share/nginx/html/*
COPY src/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]