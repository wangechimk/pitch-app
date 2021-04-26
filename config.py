import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI','postgresql+psycopg2://michellewangechi:Rosemary70@localhost/pitchapp')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    Debug = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}
