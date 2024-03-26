# To run: source venv/bin/activate (if not 'venv') + flask run, To deactivate: deactivate
# psql: start-pg.sh (run to activate in a separate terminal)
# Update schema: psql < schema.sql

from flask import Flask
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import routes
