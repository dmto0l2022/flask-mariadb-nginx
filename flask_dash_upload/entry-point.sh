#!/bin/sh
/app/env/bin/python3 flask db init
/app/env/bin/python3 flask db migrate
/app/env/bin/python3 flask db upgrade
/app/env/bin/python3 ./app/wsgi.py
