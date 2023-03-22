import os 
from sqlalchemy import create_engine

import urllib
class Config(object):
    SECRET_KEY ='MY_SECRET_KEY'
    SESSION_COOKIE_SECURE = False
 #Hacer la coneccion a la base de datos 
class DevelomentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:yerik2012@localhost:3306/idgs801_2'
    SQLALCHEMY_TRACK_MODIFICATION = False