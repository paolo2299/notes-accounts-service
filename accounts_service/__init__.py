import os

from flask import Flask
from flask_migrate import Migrate

from accounts_service import handlers
from accounts_service import database
from accounts_service.logging import setup_logging


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = database.connection_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    database.db.init_app(app)
    migrate.init_app(app, database.db)

    handlers.init_app(app)

    return app


migrate = Migrate()
setup_logging()