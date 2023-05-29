from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
import json

from app import db

from app.main import bp
from app.main.forms import *
from app.utils.general_utility import get_session_emotions

from app.models import *

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
    all_sessions = SessionData.get_all_sessions(current_user.id)

    try:
        most_recent_session = SessionData.get_most_recent_session(current_user.id)
        most_recent_session_emotions = get_session_emotions(most_recent_session)
    except:
        most_recent_session = None
        most_recent_session_emotions = None
    
    print(most_recent_session)

    try:
        therapist = Therapist.query.filter_by(id = association.therapist_id).first()
    except:
        therapist = None

    return render_template('patient_user/patient_profile.html', patient = patient, therapist = therapist, all_sessions = all_sessions, most_recent_session = most_recent_session, 
                           most_recent_session_emotions = most_recent_session_emotions)

# Everything related to viewing questionnaire data

@bp.route('/previous_phq', methods = ['GET'])
def previous_phq():
    phq9_scores = PHQ9Scores.get_all_scores(current_user.id)

    # last_10_scores = phq9_scores[-10:]

    # latest_phq_data = PHQ9Scores.get_latest_score(current_user.id)

    graph_labels = []
    score_data = []
    emotional_state_data = []

    for i in phq9_scores:
        graph_labels.append(i.time_captured.strftime('%d/%m/%Y'))
        score_data.append(i.score)
        emotional_state_data.append(i.emotional_state)

    return render_template('patient_user/previous_phq.html', graph_labels = graph_labels, score_data = score_data, emotional_state_data = emotional_state_data)

@bp.route('previous_gad', methods = ['GET'])
def previous_gad():
    return render_template('patient_user/previous_gad.html')

# Everything related to therapy sessions

@bp.route('/all_previous_sessions_page', methods = ['GET'])
def all_previous_sessions_page():
    all_sessions = SessionData.get_all_sessions(current_user.id)
    most_recent_session = SessionData.get_most_recent_session(current_user.id)

    return render_template('patient_user/all_sessions_page.html', all_sessions = all_sessions, most_recent_session = most_recent_session)

@bp.route('/specific_session/<int:session_id>', methods = ['GET'])
def specific_session(session_id):
    session = SessionData.query.get(session_id)
    emotion_data = get_session_emotions(session)

    # Here is where you should retrieve the relevant text for the emotional score and generally what it means
    session_emotions = EmotionData.get_emotion_data(session.id)
    total_emotions = len(session_emotions)

    return render_template('patient_user/specific_session_page.html', session = session, total_emotions = total_emotions, emotion_data = emotion_data, 
                           session_emotions = session_emotions)

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