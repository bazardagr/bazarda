class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    #DATABASE_URI = 'mysql://bazarda@localhostg/bazarda'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/bazarda'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://bazarda:bazarda@localhost/bazarda'

class TestingConfig(Config):
    TESTING = True