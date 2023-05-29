def get_session_emotions(session):
    emotions_count = {}
    for emotion in session.emotion_data:
        if emotion.emotion_type in emotions_count:
            emotions_count[emotion.emotion_type] += 1
        else:
            emotions_count[emotion.emotion_type] = 1
    return emotions_count