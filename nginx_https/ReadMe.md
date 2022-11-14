# create env

    cd opt
    mkdir certbot
    cd certbot
    /usr/local/bin/python3.10 -m venv env
    source env/bin/activate

# install certbot

    pip install certbot
    pip install --upgrade pip
    pip install certbot-nginx

# edit conf
    
    nano /etc/nginx/nginx.conf
    
    remove root and location /
    
# make site conf

    cd /etc/nginx/conf.d/
    nano dev3.dmtools.info.conf
    
    see example without ssl

# generate the letsencypt key files and automatically update conf

    certbot --nginx
    
    do not panic, the above finds the site and offers it for you to confirm

# as non root user

    cd /opt/dmtools/code/flask-mariadb-nginx/

    git pull
    
## clear all podman remnants in non root user
    
     podman system reset

## exit from non root user

    exit

## enter sudo

    sudo su

# as root

## clear all podman remnants in root

    podman system reset

    source clean+create.sh
    
## exit from sudo

    exit

# switch to non root user

    su agaitske --login
    
    source clean+create.sh
    
    visit https:/dev3.dmtools.info
    
    
  
  

