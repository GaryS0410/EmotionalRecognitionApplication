from flask import render_template, url_for, redirect
from flask_login import current_user, login_required

from app.therapist import bp
from app.therapist.helpers import conducted_sessions_information, get_current_patients, delete_therapist_account_data

from app.models import *

@bp.route('/therapist_dash/<int:therapist_id>', methods = ['GET'])
@login_required
def therapist_dash(therapist_id):
    if current_user.type == "therapist":
        therapist = Therapist.get_therapist(therapist_id)

        conducted_session_data = conducted_sessions_information(therapist.id)

        current_patients, patient_count = get_current_patients(therapist.id)

        return render_template('therapist_user/therapist_dash.html', therapist = therapist, current_patients = current_patients, conducted_sessions_data = conducted_session_data, 
                            patient_count = patient_count)
    else: 
        return redirect(url_for('main.landing_page'))