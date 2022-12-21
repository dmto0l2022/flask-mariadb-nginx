mkdir "/workdir/home/jupyterhub/.npm-packages"
npm config set prefix "/workdir/home/jupyterhub/.npm-packages"
export PATH="$PATH:/workdir/home/jupyterhub/.npm-packages/bin"
npm install -g configurable-http-proxy

VIRTUAL_ENV="/workdir/env"
python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

/workdir/env/bin/pip -q install pip --upgrade
/workdir/env/bin/pip install wheel

# Install dependencies:
# COPY requirements.txt /workdir/requirements.txt
/workdir/env/bin/pip install -r /workdir/requirements.txt

#RUN /workdir/env/bin/python jupyterhub --generate-config

#RUN /workdir/env/bin/activate && exec jupyterhub --generate-config

#COPY . .
COPY jupyterhub_config.py /workdir/jupyterhub/jupyterhub_config.py
#EXPOSE 8000
#CMD . /srv/jupyterhub/env/bin/activate && exec jupyterhub
#CMD . /workdir/env/bin/activate & exec jupyterhub -f /workdir/jupyterhub/jupyterhub_config.py
CMD . /workdir/env/bin/activate & exec jupyterhub --debug --config=jupyterhub_config.py
