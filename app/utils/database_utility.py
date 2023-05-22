import pytz
import datetime
from flask_login import current_user

from app import db
from app.models import SessionData

def save_session_data(emotional_score, emotion_list, image_timestamps):
    tz_uk = pytz.timezone('Europe/London')
    time_of_session = datetime.now(tz_uk)

    new_session = SessionData(user_id = current_user.id, emotional_score = emotional_score, time_of_session = time_of_session)
    db.add(new_session)
    db.session.commit()