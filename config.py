import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin123@localhost/crud_produtos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
