podman pull ubuntu:latest
podman run --name ubuntutest -dt ubuntu:latest
podman cp requirements.txt localubuntu:/requirements.txt
podman cp 1_create_with_sudo.sh ubuntutest:/1_create_with_sudo.sh
podman cp 2_create_with_user.sh ubuntutest:/2_create_with_user.sh
podman attach ubuntutest
