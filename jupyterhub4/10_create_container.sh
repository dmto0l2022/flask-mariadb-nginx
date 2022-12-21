podman pull ubuntu:latest
podman create ubuntu:latest --name localubuntu
podman cp requirements.txt localubuntu:/requirements.txt
podman cp 1_create_with_sudo.sh localubuntu:/1_create_with_sudo.sh
podman cp 2_create_with_user.sh localubuntu:/2_create_with_user.sh
podman run -it localubuntu bash
