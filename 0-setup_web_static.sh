#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

content="Wake up to Reality"
echo "$content" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

oldstr="server_name _;"
newstr="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "s|$oldstr|$newstr|" /etc/nginx/sites-enabled/default

sudo service nginx restart
