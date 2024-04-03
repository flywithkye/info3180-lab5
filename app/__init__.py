from flask import Flask
from .config import Config

from flask_sqlalchemy import SQLAlchemy

# import flask migrate here
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate = Migrate(app, db)

from app import views