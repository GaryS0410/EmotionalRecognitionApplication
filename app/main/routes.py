from flask import render_template, redirect, url_for
from flask_login import current_user, login_required

from app.main import bp
from app.main.forms import *

@bp.route('/', methods = ['GET', 'POST'])
def landing_page():
    return render_template('landing_page.html')

@bp.route('/questionnaires_page', methods = ['GET'])
@login_required
def questionnaires_page():
    return render_template('questionnaires_page.html')

@bp.route('/therapy_page', methods=['GET'])
def therapy_page():
    return render_template('therapy.html', name=current_user.first_name)

@bp.route('/model_test', methods = ['GET'])
def model_test_page():
    return render_template('model_page.html')

@bp.route('/profile_page', methods = ['GET'])
@login_required
def profile_page():
    return render_template('profile.html', name = current_user.first_name)

@bp.route('/phq9_questionnaire', methods = ['GET', 'POST'])
@login_required
def phq9_questionnaire():
    form = PHQ9Form()

    if form.validate_on_submit():
        score = form.calculate_score()
        print(score)
        return render_template('/questionnaires/PHQ9.html', score = score)
    return render_template('/questionnaires/PHQ9.html', form = form)

@bp.route('/gad7_questionnaire', methods = ['GET', 'POST'])
@login_required
def gad7_questionnaire():
    form = GAD7Form()

    if form.validate_on_submit():
        score = form.calculate_score()
        print(score)
        return render_template('/questionnaires/GAD7.html', score = score)
    return render_template('/questionnaires/GAD7.html', form = form)