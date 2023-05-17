from flask import render_template, redirect, url_for
from flask_login import current_user, login_required

from app.main import bp
from app.main.forms import *

@bp.route('/', methods = ['GET', 'POST'])
def landing_page():
    return render_template('landing_page.html')

@bp.route('/therapy_page', methods=['GET'])
def therapy_page():
    return render_template('therapy.html', name=current_user.first_name)

@bp.route('/model_test', methods = ['GET'])
def model_test_page():
    return render_template('model_page.html')

@bp.route('/profile_page', methods = ['GET'])
@login_required
def profile_page():
    return render_template('user/patient_profile.html', name = current_user.first_name)