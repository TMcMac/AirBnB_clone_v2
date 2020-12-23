#!/usr/bin/env bash
# sets up a server for webstatic

sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx restart
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Test Page for nginx" | sudo tee /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i 's|^\tlocation / {|\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {|' /etc/nginx/sites-available/default
sudo service nginx restart
