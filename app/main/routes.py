from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required

from app import db

from app.main import bp
from app.main.forms import *

from app.models import Patient, Therapist, Association

@bp.route('/', methods = ['GET', 'POST'])
def landing_page():
    return render_template('landing_page.html')

@bp.route('/therapy_page', methods=['GET'])
def therapy_page():
    therapist_list = Therapist.get_all_therapists()

    if Association.query.filter_by(patient_id = current_user.id).first():
        therapist_relationship = Association.query.filter_by(patient_id = current_user.id).first()
        therapist = Therapist.query.filter_by(id = therapist_relationship.therapist_id).first()
        therapist = therapist.first_name + " " + therapist.surname
    else: 
        therapist = None

    return render_template('therapy/therapy.html', name=current_user.first_name, therapist = therapist, therapist_list = therapist_list)

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

    association = Association.query.filter_by(patient_id = current_user.id).first()
    therapist = Therapist.query.filter_by(id = association.therapist_id).first()
    therapist = therapist.first_name + " " + therapist.surname

    return render_template('patient_user/patient_profile.html', name = full_name, email = email, therapist = therapist)

@bp.route('/choose_therapist_page', methods = ['GET', 'POST'])
@login_required
def choose_therapist_page():
    therapist_list = Therapist.query.all()

    return render_template('patient_user/choose_therapist.html', therapist_list = therapist_list, current_patient = current_user.id)

@bp.route('/assign_therapist', methods = ['POST'])
def assign_therapist():
    if request.method == 'POST':
        patient = request.form.get('patient')
        therapist = request.form.get('therapist')

        if Association.query.filter_by(patient_id = current_user.id).first():
            old_therapist_relationship = Association.query.filter_by(patient_id = current_user.id).first()
            db.session.delete(old_therapist_relationship)
            db.session.commit()

        patient_therapist_association = Association(patient_id = patient, therapist_id = therapist)
        db.session.add(patient_therapist_association)
        db.session.commit()
    else:
        return('Request failed', 400)

    flash('Therapist successfully assigned.')
    return redirect(url_for('main.profile_page'))

@bp.route('/testing_page', methods = ['GET'])
def testing_page():
    therapists = Therapist.get_all_therapists()
    print(therapists)
    return render_template('testing_page.html')