from flask import render_template
from flask_login import current_user

from app.main import bp
from app.main.forms import *

@bp.route('/', methods = ['GET', 'POST'])
def landing_page():
    return render_template('landing_page.html')

@bp.route('/homepage', methods = ['GET'])
def homepage():
    return render_template('homepage.html', first_name = current_user.first_name, email = current_user.email)

@bp.route('/questionnaires_page', methods = ['GET'])
def questionnaires_page():
    return render_template('questionnaires_page.html')