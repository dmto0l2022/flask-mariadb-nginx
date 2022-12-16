c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DummyAuthenticator.password = 'password'
c.DockerSpawner.notebook_dir = '/workdir/notebooks/'

c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.port=8000

#  Default: 'jupyterhub_config.py'
c.JupyterHub.config_file = '/workdir/jupyterhub/jupyterhub_config.py'

c.ConfigurableHTTPProxy.command = '/workdir/.npm-packages/bin/configurable-http-proxy'

# Get external IP https://stackoverflow.com/a/166589
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
c.JupyterHub.hub_connect_ip = s.getsockname()[0]
s.close()

c.DockerSpawner.image = 'docker.io/jupyter/base-notebook'
c.DockerSpawner.remove = True
