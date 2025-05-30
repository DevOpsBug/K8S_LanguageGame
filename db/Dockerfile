FROM postgres:16

# Set environment variables
ENV POSTGRES_DB=language_game
ENV POSTGRES_USER=language_game
ENV POSTGRES_PASSWORD=secret

# Copy data and import script into the default init location
COPY data.csv /docker-entrypoint-initdb.d/
COPY init.sql /docker-entrypoint-initdb.d/
