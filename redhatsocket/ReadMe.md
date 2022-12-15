# Reference

https://www.redhat.com/en/blog/painless-services-implementing-serverless-rootless-podman-and-systemd

# Commands

systemctl --user daemon-reload
systemctl --user enable --now container-httpd-proxy.socket
netstat -ltpn | grep 8080
