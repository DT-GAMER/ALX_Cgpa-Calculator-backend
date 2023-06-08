import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@hostname:port/database_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

