#!/usr/bin/env bash
# A bash script that sets up your web servers for the deployment of web_static.

sudo apt update
sudo apt install nginx -y

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/releases/test/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html
# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# changing the owner to ubuntu
sudo chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration to serve
config_text="location /hbnb_static/ {
    alias /data/web_static/current/;
}"
sudo sed -i "$config_text" /etc/nginx/sites-available/default
# nginx restsart
sudo service nginx restart
