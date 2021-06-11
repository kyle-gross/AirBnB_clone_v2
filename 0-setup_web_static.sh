#!/usr/bin/env bash
# setup webstatic deployment

var="<html>\n  <head>\n  </head>\n  <body>\n\tHolberton School\n  </body>\n</html>"
sudo mkdir /data/; sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo -e $var > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "s@^\tlocation / {@\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\n\tlocation / {@" /etc/nginx/sites-available/default