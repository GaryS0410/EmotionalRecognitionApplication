from datetime import timedelta

from app import db

from app.models import *

def determine_emotional_state(emotions):
    weighted_values = {
        'happy': -1,
        'surprise': 0,
        'disgust': 0.5,
        'neutral': 0,
        'fear': 0.5,
        'angry': 1,
        'sad': 1
    }

    total_emotion_values = sum(emotions.values())

    if total_emotion_values == 0:
        return None
    
    overall_score = 0
    for label, value in emotions.items():
        overall_score += weighted_values[label] * value
    
    emotion_score = round(overall_score / total_emotion_values, 2)
    
    return emotion_score

def categorise_emotional_state(emotional_state):
    emotions_labels_map = {
        -1: 'Extremely Positive',
        -0.75: 'Extremely Positive',
        -0.50: 'Moderately Positive',
        -0.25: 'Slightly Positive',
        0: 'Neutral',
        0.25: 'Slightly Negative',
        0.50: 'Moderately Negative',
        0.75: 'Extremely Negative',
        1: 'Extremely Negative'
    }

    rounded_score = round(emotional_state * 4) / 4

    emotion_overall = emotions_labels_map.get(rounded_score, 'Neutral')

    return emotion_overall

def save_phq9_data(score, emotional_state, patient_id):
    new_entry = PHQ9Scores(score = score, emotional_state = emotional_state, patient_id = patient_id)
    db.session.add(new_entry)
    db.session.commit()

def save_gad7_data(score, emotional_state, patient_id):
    new_entry = GAD7Scores(score = score, emotional_state = emotional_state, patient_id = patient_id)
    db.session.add(new_entry)
    db.session.commit()

def save_therapy_data(emotional_state, patient_id, therapist_id, emotion_data, image_timestamps, start_time, end_time):

    new_session_entry = SessionData(emotional_state = emotional_state, session_patient = patient_id, session_therapist = therapist_id, session_start_time = start_time,
                                    session_end_time = end_time)

    db.session.add(new_session_entry)
    db.session.commit()

    i = 0
    for emotion in emotion_data:
        new_emotiondata_entry = EmotionData(emotion_type = emotion, time_captured = image_timestamps[i], session_id = new_session_entry.id)
        db.session.add(new_emotiondata_entry)
        i += 1 
    db.session.commit()

def get_session_times(image_timestamps):
    session_start_time = image_timestamps[0]
    session_end_time = image_timestamps[-1]

    return session_start_time, session_end_time

def delete_patient_account_data(patient_id):
    patient = Patient.get_patient(patient_id)
    patient_associations = Association.get_patient_association(patient_id)
    patient_sessions = SessionData.get_all_sessions(patient_id)

    if patient_associations:
        db.session.delete(patient_associations)
        db.session.delete(patient)

        for session in patient_sessions:
            for emotion in session.emotion_data:
                db.session.delete(emotion)
            db.session.delete(session)
    else:
        db.session.delete(patient)

    db.session.commit()