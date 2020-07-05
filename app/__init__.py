import os
from flask import Flask, render_template

app = Flask(__name__)
app.config["CORE_SERVICES"] = ['cups.service']

gs = os.getenv('GUNICORN_SERVER')
if gs:
    app.config["SERVER_NAME"] = gs
else:
    app.config["SERVER_NAME"] = "127.0.0.1:8100"


from app.modules import systemd
from app.modules import watcher

from app.views import index
from app.views import services
from app.views import api
