# Create VM

make sure port forwarding is enabled

# Update VM and install dependencies

## install nano

yum install nano

## podman

    sudo yum module enable -y container-tools:rhel8
    sudo yum module install -y container-tools:rhel8
    
    yum install podman-plugins

## install dependencies

    yum install wget yum-utils make gcc openssl-devel bzip2-devel libffi-devel zlib-devel 

    yum install git
    
    yum install sqlite-devel


# Establish SSH to Host

rhel 8

ssh-keygen -t rsa -f ~/.ssh/key202204220954 -C andrew_gaitskell -b 2048

cd ~/.ssh

cat key202204220954.pub

copy output and paste into VM ssh keys

remove key202203251421.pub at start

connect to vm

ssh-keygen -f "/home/andrewcgaitskell/.ssh/known_hosts" -R "35.214.57.82"

ssh -i ~/.ssh/key202204261126 andrew_gaitskell@35.214.57.82

# Check Python Versions


upgrade python

wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz 

tar xzf Python-3.10.4.tgz 

cd Python-3.10.4

./configure --with-system-ffi --with-computed-gotos --enable-loadable-sqlite-extensions

./configure --enable-optimizations

make -j ${nproc} 
make altinstall

create env

/usr/local/bin/python3.10 -m venv env

upgrade pip

/home/andrew_gaitskell/Python-3.10.4/env/bin/python3.10 -m pip install --upgrade pip

enable env

    source env/bin/activate
