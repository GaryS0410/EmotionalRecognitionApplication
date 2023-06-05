from flask import render_template
from flask_login import current_user, login_required

from app.therapist import bp
from app.models import *

@bp.route('/therapist_dash', methods = ['GET'])
@login_required
def therapist_dash():
    therapist = Therapist.query.filter_by(id = current_user.id).first()

    current_patient_associations = Association.get_therapist_associations(current_user.id)
    conducted_sessions = SessionData.get_therapist_sessions(current_user.id)
    
    conducted_session_patients = []
    for i in conducted_sessions:
        current_patient = Patient.query.filter_by(id = i.session_patient).first()
        conducted_session_patients.append(current_patient)

    patient_count = len(current_patient_associations)

    current_patients = []

    conducted_session_data = zip(conducted_sessions, conducted_session_patients)

    if current_patient_associations is not None:
        for association in current_patient_associations:
            patient = Patient.get_patient(association.patient_id)
            current_patients.append(patient)

    return render_template('therapist_user/therapist_dash.html', therapist = therapist, current_patients = current_patients, conducted_sessions_data = conducted_session_data, 
                           patient_count = patient_count)

@bp.route('/view_patient_details', methods = ['GET'])
def view_patient_details():
    return "<h4> Patient Details Page </h4>"