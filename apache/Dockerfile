FROM httpd:latest

# Create log directories and set permissions correctly
RUN mkdir -p /usr/local/apache2/logs \
    && chmod -R 777 /usr/local/apache2/logs \
    && chown -R daemon:daemon /usr/local/apache2/logs

# Copy proxy configuration file
COPY apache.conf /usr/local/apache2/conf/httpd.conf

# Add entrypoint script to change permissions at runtime
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]


