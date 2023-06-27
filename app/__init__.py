from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# from . import config
from .config import Config

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app(config_class = Config):
    app = Flask(__name__, static_url_path='/static', static_folder='static')

    app.config.from_object(config_class)

    db.init_app(app)

    from app.main import bp as main_bp
    from app.auth import bp as auth_bp
    from app.therapist import bp as therapist_bp
    from app.errors import bp as errors_bp

    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(therapist_bp, url_prefix='/')
    app.register_blueprint(errors_bp, url_prefix='/')

    from app.models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

