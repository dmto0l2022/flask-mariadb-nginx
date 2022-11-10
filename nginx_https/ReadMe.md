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
    
    source create5000.sh
  
  

