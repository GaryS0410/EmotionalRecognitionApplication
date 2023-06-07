from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import patient_routes, questionnaire_routes, therapy_routes