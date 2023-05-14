from flask import render_template
from flask_login import current_user, login_required

from app.main import bp
from app.main.forms import *

@bp.route('/', methods = ['GET', 'POST'])
def landing_page():
    return render_template('landing_page.html')

@bp.route('/homepage', methods = ['GET'])
@login_required
def homepage():
    return render_template('homepage.html', first_name = current_user.first_name, email = current_user.email)

@bp.route('/questionnaires_page', methods = ['GET'])
@login_required
def questionnaires_page():
    return render_template('questionnaires_page.html')

@bp.route('/model_test', methods = ['GET'])
def model_test_page():
    return render_template('model_page.html')