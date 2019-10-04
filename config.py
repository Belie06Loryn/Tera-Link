import os
class Config:
    
    SECRET_KEY = ('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/teras'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
  

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/tera_test'


class ProdConfig(Config):
   
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexie:root@localhost/teras'

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
