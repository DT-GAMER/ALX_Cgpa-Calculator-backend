import os

class Config:
    SECRET_KEY = os.environ.get('fSjjF9k34XAC1RgVJBd8xvEezU7yqd')
    SQLALCHEMY_DATABASE_URI = 'postgres://gradeccalculator-main-db-0b2e170f6fc37da17:fSjjF9k34XAC1RgVJBd8xvEezU7yqd@user-prod-us-east-2-1.cluster-cfi5vnucvv3w.us-east-2.rds.amazonaws.com:5432/gradeccalculator-main-db-0b2e170f6fc37da17'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

