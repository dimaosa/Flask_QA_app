# default config
import os

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\x15\xc8A\xdc\x17\xea0\x84\xd6\xc1\xab:\xf4\xd7e\x94\x1b\x90\xfb[\x9e5\x1a\xd7'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False	
		