import os

class Config :
  '''
  Genarate configuration parent class
  '''
  SECRET_KEY ="anitha"
 
class ProdConfig(Config):

  pass

class DevConfig(Config):
 
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:1234@localhost/Tera'
  DEBUG = True
class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:1234@localhost/Tera'
config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
  }  
 