import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = "SECRET PASS"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Gtagomez1@localhost:3306/bdidgs805"
    SQLALCHEMY_TRACK_MODIFICATIONS = False