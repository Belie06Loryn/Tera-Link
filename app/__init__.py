from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_uploads import UploadSet,configure_uploads,IMAGES
from config import config_options

db = SQLAlchemy()
# photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    db.init_app(app)
    # configure_uploads(app,photos)
    return app
