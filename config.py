import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = "SECRET PASS"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    sqlalchemy_database_uri = "mysql+pymysql://root:jjdgrlepc2003@localhost:3307/bdidgs805"
    SQLALCHEMY_TRACK_MODIFICATIONS = False