import os
class Config:
  """General configuration parent class"""
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

  # email configuration
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 25
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
  """Production configuration child class
  Args:
    Config:The parent configuration class with General configuration settings
  """
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

class DevConfig(Config):
  """
  Development configuration child class
  Args:
    Config:The parent configuration class with General configuration settings
  """
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}