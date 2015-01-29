# default config
import os

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = os.urandom(24)
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False	
		