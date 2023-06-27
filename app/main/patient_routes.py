from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
import json

from app import db

from app.main import bp
from app.main.forms import *
from app.models import *
from app.main.helpers import delete_account_data

# Landing page route 

@bp.route('/', methods = ['GET', 'POST'])
def landing_page():
    return render_template('landing_page.html')

# All patient profile related pages/routes. Maybe will let these be accessed by therapist as well? Dunno yet
@bp.route('/profile_page/<int:patient_id>', methods = ['GET', 'POST'])
@login_required
def profile_page(patient_id):
    # Getting current patient by querying the database with the current user id
    patient = Patient.get_patient(patient_id)
    
    association = Association.get_patient_association(patient.id)

    if association is not None:
        therapist = Therapist.get_therapist(association.therapist_id)
    else:
        therapist = None

    all_sessions = SessionData.get_all_sessions(patient.id)
    most_recent_session = SessionData.get_most_recent_session(patient_id = patient.id)

    if most_recent_session:
        most_recent_session_emotions = SessionData.get_session_emotions(most_recent_session)
    else:
        most_recent_session_emotions = None

    most_recent_phq = PHQ9Scores.get_latest_score(patient.id)
    most_recent_gad = GAD7Scores.get_latest_score(patient.id)

    return render_template('patient_user/patient_profile.html', patient = patient, therapist = therapist, 
                           all_sessions = all_sessions, most_recent_session = most_recent_session, 
                           most_recent_session_emotions = most_recent_session_emotions, 
                           most_recent_phq = most_recent_phq, most_recent_gad = most_recent_gad)

# Everything related to viewing questionnaire data

@bp.route('/previous_phq/<int:patient_id>', methods = ['GET'])
@login_required
def previous_phq(patient_id):
    patient = Patient.get_patient(patient_id)
    phq9_scores = PHQ9Scores.get_all_scores(patient.id)
    most_recent = PHQ9Scores.get_latest_score(patient.id)

    graph_labels = []
    score_data = []
    emotional_state_data = []

    for i in phq9_scores:
        graph_labels.append(i.time_captured.strftime('%d/%m/%Y'))
        score_data.append(i.score)
        emotional_state_data.append(i.emotional_state)

    return render_template('patient_user/previous_phq.html', graph_labels = graph_labels, score_data = score_data, emotional_state_data = emotional_state_data,
                           most_recent = most_recent)

@bp.route('previous_gad/<int:patient_id>', methods = ['GET'])
@login_required
def previous_gad(patient_id):
    patient = Patient.get_patient(patient_id)
    
    gad7_scores = GAD7Scores.get_all_scores(patient.id)
    most_recent = GAD7Scores.get_latest_score(patient.id)

    graph_labels = []
    score_data = []
    emotional_state_data = []

    for i in gad7_scores:
        graph_labels.append(i.time_captured.strftime('%d/%m/%Y'))
        score_data.append(i.score)
        emotional_state_data.append(i.emotional_state)

    return render_template('patient_user/previous_gad.html', graph_labels = graph_labels, score_data = score_data, emotional_state_data = emotional_state_data, 
                           most_recent = most_recent)

# Everything related to therapy sessions

@bp.route('/specific_session/<int:session_id>', methods = ['GET'])
@login_required
def specific_session(session_id):
    session = SessionData.query.get(session_id)
    emotion_data = SessionData.get_session_emotions(session)
    session_therapist = Therapist.get_therapist(session.session_therapist)
    session_patient = Patient.get_patient(session.session_patient)

    # Here is where you should retrieve the relevant text for the emotional score and generally what it means
    session_emotions = EmotionData.get_emotion_data(session.id)
    total_emotions = len(session_emotions)

    return render_template('patient_user/specific_session_page.html', session = session, 
                           total_emotions = total_emotions, emotion_data = emotion_data, 
                           session_emotions = session_emotions, session_therapist = session_therapist, 
                           session_patient = session_patient)

# Choosing/updating therapist related functionality 

@bp.route('/choose_therapist_page', methods = ['GET', 'POST'])
@login_required
def choose_therapist_page():
    therapist_list = Therapist.get_all_therapists()
    
    if len(therapist_list) == 0:
        therapist_list = None

    return render_template('patient_user/choose_therapist.html', therapist_list = therapist_list, current_patient = current_user.id)

    return render_template('patient_user', patient = patient)

@bp.route('/assign_therapist', methods = ['POST'])
@login_required
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
        print(patient_therapist_association)
    else:
        return('Request failed', 400)

    flash('Therapist successfully assigned.')
    return redirect(url_for('main.profile_page', patient_id = current_user.id))

@bp.route('/delete_patient_account/<int:patient_id>', methods = ['GET', 'POST'])
@login_required
def delete_account(patient_id):
    delete_account_data(patient_id)
    return redirect(url_for('main.landing_page'))