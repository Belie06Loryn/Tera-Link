from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()
# Initializing application

def create_app(config_name):
  app = Flask(__name__)

 # Setting up configuration
  app.config.from_object(config_options[config_name])
  app.config.from_pyfile("config.py")

  # Initializing flask extensions
  bootstrap.init_app(app)
  db.init_app(app)
  return app
