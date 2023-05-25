from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required

from app import db

from app.main import bp
from app.main.forms import *
from app.utils.general_utility import get_recent_session_emotions

from app.models import Patient, Therapist, Association, SessionData

# Landing page route 

@bp.route('/', methods = ['GET', 'POST'])
def landing_page():
    return render_template('landing_page.html')

# All patient profile related pages/routes. Maybe will let these be accessed by therapist as well? Dunno yet

@bp.route('/profile_page', methods = ['GET'])
@login_required
def profile_page():
    patient = Patient.query.filter_by(id = current_user.id).first() 
    association = Association.query.filter_by(patient_id = current_user.id).first()
    all_sessions = SessionData.get_all_sessions(patient_id = current_user.id)

    try:
        most_recent_session = SessionData.get_most_recent_session(patient_id = current_user.id)
        most_recent_session_emotions = get_recent_session_emotions(most_recent_session)
    except:
        most_recent_session = None
        most_recent_session_emotions = None

    try:
        therapist = Therapist.query.filter_by(id = association.therapist_id).first()
    except:
        therapist = None

    return render_template('patient_user/patient_profile.html', patient = patient, therapist = therapist, all_sessions = all_sessions, most_recent_session = most_recent_session, 
                           most_recent_session_emotions = most_recent_session_emotions)

# Everything related to viewing questionnaire data

@bp.route('/previous_phq', methods = ['GET'])
def previous_phq():
    return render_template('patient_user/previous_phq.html')

@bp.route('previous_gad', methods = ['GET'])
def previous_gad():
    return render_template('patient_user/previous_gad.html')

# Everything related to therapy sessions

@bp.route('/all_previous_sessions_page', methods = ['GET'])
def all_previous_sessions_page():
    all_sessions = SessionData.get_all_sessions(current_user.id)
    most_recent_session = SessionData.get_most_recent_session(current_user.id)

    return render_template('patient_user/all_sessions_page.html', all_sessions = all_sessions, most_recent_session = most_recent_session)

@bp.route('/specific_session', methods = ['GET'])
def specific_session():
    return None

# Choosing/updating therapist related functionality 

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
            old_therapist_id = old_therapist_relationship.therapist_id

            db.session.delete(old_therapist_relationship)
            db.session.commit()

        patient_therapist_association = Association(patient_id = patient, therapist_id = therapist)
        db.session.add(patient_therapist_association)
        db.session.commit()
    else:
        return('Request failed', 400)

    flash('Therapist successfully assigned.')
    return redirect(url_for('main.profile_page'))