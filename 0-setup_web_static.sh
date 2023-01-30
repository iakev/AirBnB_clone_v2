#!/usr/bin/env bash
# Setting up we servers for web_static deployment

# installing nginx
sudo apt -y update
sudo apt install -y nginx

#creating requisute folders
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

#creating a placeholder html file
echo "<html>
	<head>
	</head>
	<body>
		 Holberton School
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

#create a symbolic link if exists delete and recreate it
symfile="/data/web_static/current"
if [ -L $symfile ]; then
    sudo rm $symfile
fi

sudo ln -s /data/web_static/releases/test $symfile

#give ownership of /data/ recursively to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

#Update Nginx configuration to serve content of /data/web_static/current/ to
#hbnh_static
sudo echo "# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
server {
       listen 80;
       listen [::]:80;

       server_name iakevdesign.tech;

       root /var/www/iakevdesign.tech/text;
       index hello index.html;

       # Everything is a 404
       location / {
       		try_files \$uri \$uri/ =404;
       }

       location /redirect_me {
       		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	error_page 404 /error;
	location = /error {
		 root /var/www/iakevdesign.tech/text;
		 internal;
	}
       	location ^~ /hbnb_static {
		alias /data/web_static/current;
	}
}" | sudo tee /etc/nginx/sites-available/iakevdesign.tech > /dev/null

#restarting nginx for changes in conf to take hold
sudo service nginx restart
