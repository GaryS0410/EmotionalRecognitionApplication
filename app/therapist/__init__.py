from flask import Blueprint

bp = Blueprint('therapist', __name__)

from app.therapist import routes