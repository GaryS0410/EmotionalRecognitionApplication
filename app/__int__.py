from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManagers

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__, static_url_path='/static', static_folder='static')

    app.init_app(app)
    
    from 