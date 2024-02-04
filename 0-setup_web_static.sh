#!/usr/bin/env bash
# a Bash script  sets up your web servers for the deployment of web_stati

apt-get -y update > /dev/null
apt-get install -y nginx > /dev/null

# Creates necessary directories and files
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Hello World again!" > /data/web_static/releases/test/index.html

# Check if directory current exist or not
if [ -d "/data/web_static/current" ]
then
        sudo rm -rf /data/web_static/current
fi
# Create a symbolic link to test
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Changing ownership to user ubuntu
chown -hR ubuntu:ubuntu /data

# Configuring nginx to serve content pointed to by a symbolic link to hbnb_static
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restartting server
service nginx restart