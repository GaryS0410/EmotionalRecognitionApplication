from flask import Blueprint

bp = Blueprint('utility', __name__)

from app.utils import image_utility