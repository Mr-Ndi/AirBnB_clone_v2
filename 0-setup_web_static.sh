#!/bin/bash
# Update the system and install Nginx
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary folders if they don't already exist
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content
config_text="location /hbnb_static/ {
    alias /data/web_static/current/;
}"
sudo sed -i "/server {/a $config_text" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
