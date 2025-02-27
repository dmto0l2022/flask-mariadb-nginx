import os

#c = get_config()

#  Default: 'jupyterhub_config.py'
c.JupyterHub.config_file = '/workdir/jupyterhub/jupyterhub_config.py'

## File in which to store the cookie secret.
#  Default: 'jupyterhub_cookie_secret'
c.JupyterHub.cookie_secret_file = '/workdir/jupyterhub/jupyterhub_cookie_secret'
c.ConfigurableHTTPProxy.pid_file = '/workdir/jupyterhub/jupyterhub-proxy.pid'

# We rely on environment variables to configure JupyterHub so that we
# avoid having to rebuild the JupyterHub container every time we change a
# configuration parameter.

# Spawn single-user servers as Docker containers
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

# Spawn containers from this image
c.DockerSpawner.image = 'jupyterhub/singleuser:latest'

# JupyterHub requires a single-user instance of the Notebook server, so we
# default to using the `start-singleuser.sh` script included in the
# jupyter/docker-stacks *-notebook images as the Docker run command when
# spawning containers.  Optionally, you can override the Docker run command
# using the DOCKER_SPAWN_CMD environment variable.
# spawn_cmd = os.environ.get("DOCKER_SPAWN_CMD", "start-singleuser.sh")
# c.DockerSpawner.cmd = spawn_cmd

# Connect containers to this Docker network
network_name = 'jupyter_network'
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name

# Explicitly set notebook directory because we'll be mounting a volume to it.
# Most jupyter/docker-stacks *-notebook images run the Notebook server as
# user `jovyan`, and set the notebook directory to `/home/jovyan/work`.
# We follow the same convention.
notebook_dir = "/workdir/notebooks
c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}

# Remove containers once they are stopped
c.DockerSpawner.remove = True

# For debugging arguments passed to spawned containers
c.DockerSpawner.debug = True

# User containers will access hub by container name on the Docker network
c.JupyterHub.hub_ip = "jupyterhub"
c.JupyterHub.hub_port = 8000

# Persist hub data on volume mounted inside container
c.JupyterHub.cookie_secret_file = "/workdir/data/jupyterhub_cookie_secret"
c.JupyterHub.db_url = "sqlite://///workdir/data/jupyterhub.sqlite"

# Authenticate users with Native Authenticator
c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"

# Allow anyone to sign-up without approval
c.NativeAuthenticator.open_signup = True

# Allowed admins
admin = 'jupyterhub'
if admin:
    c.Authenticator.admin_users = [admin]

c.JupyterHub.bind_url = 'http://0.0.0.0:8000/'
