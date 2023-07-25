import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'temp_keydsfdfdf3489%^&'

    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://root:12345@localhost/supermarket_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
