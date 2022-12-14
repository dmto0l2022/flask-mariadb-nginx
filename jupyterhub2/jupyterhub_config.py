c.JupyterHub.authenticator_class = "dummy"
c.JupyterHub.spawner_class = "docker"
c.JupyterHub.hub_ip = '0.0.0.0'

# Get external IP https://stackoverflow.com/a/166589
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
c.JupyterHub.hub_connect_ip = s.getsockname()[0]
s.close()

c.DockerSpawner.image = 'docker.io/jupyter/base-notebook'
c.DockerSpawner.remove = True
