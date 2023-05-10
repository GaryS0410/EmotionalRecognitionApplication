from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from . import config

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__, static_url_path='/static', static_folder='static')

    app.config.from_object(config.Config)

    db.init_app(app)

    from app.main import bp as main_bp
    from app.errors import bp as errors_bp

    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(errors_bp, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app