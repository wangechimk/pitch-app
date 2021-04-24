class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wangechimk@localhost/pitches'

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
