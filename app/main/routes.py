from flask import render_template, request
from flask_login import current_user, login_required

from app import db

from app.main import bp
from app.main.forms import *

from app.models import Therapist, Association

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
    first_name = current_user.first_name 
    surname = current_user.surname

    full_name = first_name + " " + surname
    email = current_user.email

    therapist_association = Association.get_associations_patient(patient_id = current_user.id)
    therapist = Therapist.query.filter_by(id = therapist_association.therapist_id)
    print(therapist.first_name)

    return render_template('patient_user/patient_profile.html', name = full_name, email = email)

@bp.route('/choose_therapist_page', methods = ['GET', 'POST'])
@login_required
def choose_therapist_page():
    therapist_list = Therapist.query.all()
    current_patient = current_user.id

    return render_template('patient_user/choose_therapist.html', therapist_list = therapist_list, current_patient = current_patient)

# Also need to make the actual bloody functionality to work
# Must add additional functionality here to account for patient already having an assigned therapist (should be easy enough)
@bp.route('/assign_therapist', methods = ['POST'])
def assign_therapist():
    if request.method == 'POST':
        patient = request.form.get('patient')
        therapist = request.form.get('therapist')

        patient_therapist_association = Association()
        db.session.add(patient_therapist_association)
        db.session.commit()
    else:
        return('Request failed', 400)

    return('Therapist successfully assigned to patient', 200)