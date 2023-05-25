from datetime import datetime

from app import db

from app.models import GAD7Scores, PHQ9Scores, SessionData, EmotionData

# Function for calculating "emotional score metric". This is a holdover from v1 of the application,
# and therefore is subject to change. Haven't ever been fully happy with how this works, however
# I am really struggling to think of another way. It's good enough for now.
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

# Function for saving a questionnaire attempt 
def save_questionnaire_data(questionnaire_type, score, emotional_state, patient_id):
    try: 
        if questionnaire_type == "PHQ":
            new_entry = PHQ9Scores(score = score, emotional_state = emotional_state, patient_id = patient_id)
            db.session.add(new_entry)
            db.commit()
        elif questionnaire_type == "GAD":
            new_entry = GAD7Scores(score = score, emotional_state = emotional_state, patient_id = patient_id)
            db.session.add(new_entry)
            db.commit()
    except:
        print("An error has occured while trying to save the questionnaire attempt")


# Function for saving a therapy session
def save_therapy_data(emotional_state, patient_id, therapist_id, emotion_data, image_timestamps):
    new_session = SessionData(time_of_session = datetime.now(), emotional_state = emotional_state, patient_id = patient_id, therapist_id = therapist_id)

    db.session.add(new_session)
    db.session.commit()

    i = 0
    for emotion in emotion_data:
        print(i)
        new_emotiondata_entry = EmotionData(emotion_type = emotion, time_captured = image_timestamps[i], session_id = new_session.id) 
        db.session.add(new_emotiondata_entry)
        i += 1
    db.session.commit()