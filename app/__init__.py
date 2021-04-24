from flask import Flask
from config import config_options
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.static_folder = 'static'
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.load_view = 'auth.login'


def create_app(config_name):
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    # from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint
    #
    # app.register_blueprint(authentication_blueprint)
    app.register_blueprint(main_blueprint)

    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    return app
