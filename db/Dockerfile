FROM postgres:16

# Expected environment variables:
# ENV POSTGRES_DB
# ENV POSTGRES_USER
# ENV POSTGRES_PASSWORD

# Copy data and import script into the default init location
RUN mkdir -p /init/csv/
COPY ./data/*.csv /init/csv/
COPY ./combine_csv_files.sh /init/
RUN chmod +x /init/combine_csv_files.sh
# Run the script to combine CSV files into a single file
RUN /init/combine_csv_files.sh -i /init/csv/ -o /docker-entrypoint-initdb.d/data.csv
COPY init.sql /docker-entrypoint-initdb.d/
