import os


class Config:
    SECRET_KEY = 'jason'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'leongjason822@gmail.com'
    MAIL_PASSWORD = '378100Yc'
