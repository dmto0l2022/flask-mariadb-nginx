# Create VM

make sure port forwarding is enabled

## Command Line

gcloud compute instances create fedora-vm-1 --project=proj-dmtools-1 --zone=europe-west2-c --machine-type=e2-medium --network-interface=address=35.214.101.196,network-tier=STANDARD,subnet=default --can-ip-forward --maintenance-policy=MIGRATE --provisioning-model=STANDARD --service-account=1002786492798-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server,https-server --create-disk=auto-delete=yes,boot=yes,device-name=fedora-vm-1,image=projects/fedora-cloud/global/images/fedora-cloud-base-gcp-36-20220506-n-0-x86-64,mode=rw,size=10,type=projects/proj-dmtools-1/zones/europe-west2-c/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any

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
