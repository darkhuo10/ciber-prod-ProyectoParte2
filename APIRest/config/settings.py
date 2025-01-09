# settings.py
import os
from config.variables import cargarvariables

SECRET_KEY = 'you-will-never-guess'
DEBUG=True

cargarvariables()
SQLALCHEMY_DATABASE_URI = f'mariadb+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'

SQLALCHEMY_TRACK_MODIFICATIONS = False
