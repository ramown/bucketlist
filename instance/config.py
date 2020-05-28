"""config.py."""
import os


class Config:
    """Parent Configuration class."""

    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_DATABASE_URI = "sqlite:///flask_api.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configurations for development."""

    SQLALCHEMY_ECHO = True
    DEBUG = True


class TestingConfig(Config):
    """onfigurations for Testing, with a separate test databse."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_db.db"
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""

    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
