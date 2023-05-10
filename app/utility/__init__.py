from flask import Blueprint

bp = Blueprint('utility', __name__)

from app.utility import image_utility