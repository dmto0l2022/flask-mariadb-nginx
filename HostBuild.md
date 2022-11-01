# Fedora VM Installation and Rebuild

# Host Information
* OS: Pop!_OS 21.10
* VM Software: Gnome Boxes 42.1-6668d79d (Flatpak)

# update

sudo yum update

# Installation
## Install system dependencies  

      sudo dnf install httpd httpd-devel mariadb mariadb-server mariadb-connector-c-devel \
      python3-devel

      sudo yum install git
      sudo yum install gcc
      sudo yum install nano
      sudo yum install openssl


## Enable the database service

      sudo systemctl enable mariadb
      sudo systemctl start mariadb

## Create the database
     sudo mysql_secure_installation`
     There will originally be no SQL root password, so just hit enter
     Then establish the SQL root password listed above
     sudo mysql -u root -p`
     Enter database root password
   
## Restore the database from a backup  

     sudo mysql DMTools -u root -p < dmtools_limitsonly.sql

## Create a virtual environment for the project  

     python -m venv env

## Update the `.gitignore` file to ignore `dmtools_env/`

## Activate the environment  

      source env/bin/activate

## Install Python dependencies  

    pip install django mod-wsgi mysqlclient
    
    pip install -r requirements.txt 



cp -r /home/andrew_gaitskell/secrets /home/andrew_gaitskell/Projects/DMTools1/djangoapp1


## Copy `settings.py` to `settings.example.py`

## Add `secrets.json to `.gitignore`

## Edit `settings.py` to use `secrets.json`

      
## gunicorn

      https://realpython.com/django-nginx-gunicorn/
      
      some of the above was useful, it over complicates in parts
      
      pip install gunicorn
      
      ""DMTools1/djangoapp1/config/gunicorn/dev.py"""

            """Gunicorn *development* config file"""

            # Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
            wsgi_app = "dmtools1.wsgi:application"
            # The granularity of Error log outputs
            loglevel = "debug"
            # The number of worker processes for handling requests
            workers = 2
            # The socket to bind
            bind = "0.0.0.0:8080"
            # Restart workers when code changes (development only!)
            reload = True
            # Write access and error info to /var/log
            accesslog = errorlog = "/home/andrew_gaitskell/log/gunicorn/dev.log"
            # Redirect stdout/stderr to log file
            capture_output = True
            # PID file so you can easily fetch process ID
            pidfile = "/home/andrew_gaitskell/run/gunicorn/dev.pid"
            # Daemonize the Gunicorn process (detach & enter background)
            daemon = True
      
      
      gunicorn -c config/gunicorn/dev.py
      nano /home/andrew_gaitskell/log/gunicorn/dev.log
      pkill gunicorn
      nano /home/andrew_gaitskell/log/gunicorn/dev.log

      cd /etc/sysconfig
      
      sudo nano selinux
      
      set SELINUX=disabled

## nginx

      cd /etc/nginx/conf.d
      
      sudo nano dmtools.info.conf
                                                          
            server_tokens               off;
            access_log                  /var/log/nginx/dmtools.access.log;
            error_log                   /var/log/nginx/dmtools.error.log;

            # This configuration will be changed to redirect to HTTPS later
            server {
                    server_name               dev1.dmtools.info;
                    listen                    80;
                    location /app/ {
                            proxy_pass              http://127.0.0.1:8080/;
                            proxy_set_header        Host $host;
                               }
                    }


# add app to settings.py

      https://stackoverflow.com/questions/28147916/how-to-host-a-django-project-in-a-subpath
      
      FORCE_SCRIPT_NAME = '/app'



# RUN

            cd /home/andrew_gaitskell/Projects/DMTools1/

            gunicorn -c config/gunicorn/dev.py

            sudo pkill gunicorn

# Diagnostics
 
    nano /var/log/nginx/dmtools.error.log
    sudo nano /var/log/gunicorn/dev.log
    
    
# letsencrypt

# github social auth

# GUNICORN as Service

# Add GUNICORN to Docker Container
