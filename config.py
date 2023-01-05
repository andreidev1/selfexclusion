"""Flask configuration variables."""
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    SERVER_NAME = environ.get("SERVER_NAME")

    # Database
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production config for Flask app"""

    FLASK_ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    UPLOAD_FOLDER = environ.get("UPLOAD_FOLDER")


class DevelopmentConfig(Config):
    """Development config for Flask app"""

    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    DEV_UPLOAD_FOLDER = environ.get("DEV_UPLOAD_FOLDER")


    

class TestingConfig(Config):
    """Testing config for Flask app"""

    FLASK_ENV = 'development'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get("TEST_DATABASE_URI")
    TEST_UPLOAD_FOLDER = environ.get("TEST_UPLOAD_FOLDER")

