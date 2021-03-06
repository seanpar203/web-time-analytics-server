import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Config
app = Flask(__name__)

CORS(app)
app_settings = os.getenv('APP_SETTINGS', 'wta_app.config.DevConfig')
app.config.from_object(app_settings)

# DB Connection
db = SQLAlchemy(app)

# Blueprints
from wta_app.time_spent.views import times

app.register_blueprint(times)
