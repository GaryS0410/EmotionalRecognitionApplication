from flask import render_template
from flask_login import current_user

from app.therapist import bp
from app.models import *

@bp.route('/therapist_dash', methods = ['GET'])
def therapist_dash():
    current_patient_associations = Association.get_associations_therapist(current_user.id)

    current_patients = []
    for association in current_patient_associations:
        patient = Patient.get_patient(association.patient_id)
        current_patients.append(patient)

    return render_template('therapist_user/therapist_dash.html', current_patients = current_patients)

@bp.route('/view_patient_details', methods = ['GET'])
def view_patient_details():
    return "<h4> Patient Details Page </h4>"