#!/usr/bin/env bash
# Preparing server for deployment

# Update/upgrade
sudo apt-get -y update
sudo apt-get -y upgrade

# Install nginx
sudo apt-get -y install nginx
sudo service nginx start

# Create paths
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create fake HTML index file
sudo echo "Hello" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

# Change ownership
sudo chown -R ubuntu:ubuntu /data/

# Edit nginx config file
searchStr="^\tlocation / {"
replaceStr="\tlocation /hbnb_static/ {\n\
\t\talias /data/web_static/current/;\n\
\t}\n\n\
\tlocation / {"
sudo sed -i "s@$searchStr@$replaceStr@" /etc/nginx/sites-available/default

sudo service nginx restart

exit 0