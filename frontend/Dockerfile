# Use a small official NGINX image
FROM nginx:alpine

# Remove the default NGINX static files
RUN rm -rf /usr/share/nginx/html/*

# Copy static assets from the src directory to the NGINX web root
COPY src/ /usr/share/nginx/html

# Replace NGINX default config
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the default NGINX port
EXPOSE 80

# Use default CMD and entrypoint from nginx
