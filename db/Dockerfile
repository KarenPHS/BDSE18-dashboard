# Derived from official mysql image (our base image)
FROM mysql

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup

COPY ./data_with_database/ /docker-entrypoint-initdb.d/

