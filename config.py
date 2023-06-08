import os

class Config:
    SECRET_KEY = os.environ.get('bvUx^L7@3L#t^Z4n')
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@hostname:port/database_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

