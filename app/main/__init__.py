from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes, questionnaire_routes, therapy_routes