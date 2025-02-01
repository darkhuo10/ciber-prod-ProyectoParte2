#!/bin/sh
# Ensure log directory exists and has correct permissions
mkdir -p /usr/local/apache2/logs
chown -R daemon:daemon /usr/local/apache2/logs
chmod -R 777 /usr/local/apache2/logs

# Start Apache in the foreground
httpd-foreground
