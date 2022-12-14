FROM jupyterhub/jupyterhub:latest

# Install dockerspawner, nativeauthenticator
RUN python3 -m pip install --no-cache-dir \
        dockerspawner==12.* \
        jupyterhub-nativeauthenticator==1.*

CMD ["jupyterhub", "-f", "/workdir/jupyterhub/jupyterhub_config.py"]
