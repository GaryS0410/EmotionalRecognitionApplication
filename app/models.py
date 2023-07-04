from flask_login import UserMixin
from sqlalchemy.sql import func 
from datetime import datetime

from . import db

class Association(db.Model):
    __tablename__ = 'Association'
    id = db.Column(db.Integer, primary_key = True)
    patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))
    therapist_id = db.Column(db.Integer, db.ForeignKey('Therapist.id'))

    @staticmethod
    def get_therapist_associations(therapist_id):
        association = Association.query.filter_by(therapist_id = therapist_id).all()
        return association

    @staticmethod
    def get_patient_association(patient_id):
        association = Association.query.filter_by(patient_id = patient_id).first()
        return association

# Model for EmotionData database table. Is used in order to capture a emotion, 
# it's type, and its timestamp. Has a relationshhip to the SessionData table
class EmotionData(db.Model):
    __tablename__ = 'EmotionData'
    id = db.Column(db.Integer, primary_key=True)
    emotion_type = db.Column(db.String(20), nullable=False)
    time_captured = db.Column(db.DateTime(timezone=True), default=func.now())
    session_id = db.Column(db.Integer, db.ForeignKey('SessionData.id'))

    @staticmethod
    def get_emotion_data(session_id):
        emotion_data = EmotionData.query.filter_by(session_id = session_id).all()
        return emotion_data

# Model for SessionData database table. It is used in order to log details of a
# therapy session, such as the emotional score, its time, the user, etc.
class SessionData(db.Model):
    __tablename__ = 'SessionData'
    id = db.Column(db.Integer, primary_key=True)
    session_start_time = db.Column(db.DateTime(timezone=True), default=func.now())
    session_end_time = db.Column(db.DateTime(timezone=True), default=func.now())
    emotional_state = db.Column(db.String(50))
    session_patient = db.Column(db.Integer, db.ForeignKey('Patient.id'))
    session_therapist = db.Column(db.Integer, db.ForeignKey('Therapist.id'))
    emotion_data = db.relationship('EmotionData')

    @staticmethod
    def get_all_sessions(patient_id):
        return SessionData.query.filter_by(session_patient = patient_id).all()

    @staticmethod
    def get_most_recent_session(patient_id):
        try:
            most_recent_session = SessionData.query.filter_by(session_patient = patient_id).order_by(SessionData.session_start_time.desc()).first()
            return most_recent_session
        except:
            return None
        
    @staticmethod
    def get_therapist_sessions(therapist_id):
        conducted_sessions = SessionData.query.filter_by(session_therapist = therapist_id).all()
        if len(conducted_sessions) > 0:
            return conducted_sessions
        else:
            return None
    
    @staticmethod
    def get_session_emotions(session):
        try:
            emotions_count = {}
            for emotion in session.emotion_data:
                if emotion.emotion_type in emotions_count:
                    emotions_count[emotion.emotion_type] += 1
                else: 
                    emotions_count[emotion.emotion_type] = 1
            return emotions_count
        except:
            return None

# Model for PHQ9Scores. Used to store the score, emotional_score, time when the 
# questionnaire was done, etc.
class PHQ9Scores(db.Model):
    __tablename__ = 'PHQ9Scores'
    id = db.Column(db.Integer, primary_key = True)
    score = db.Column(db.Integer, nullable = False)
    emotional_state = db.Column(db.Integer, nullable = False)
    time_captured = db.Column(db.DateTime(timezone=True), default=func.now())
    patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))

    @staticmethod
    def get_all_scores(patient_id):
        return PHQ9Scores.query.filter_by(patient_id = patient_id).order_by(PHQ9Scores.time_captured.asc()).all()
    
    @staticmethod
    def get_latest_score(patient_id):
        all_scores = PHQ9Scores.query.filter_by(patient_id = patient_id).order_by(PHQ9Scores.time_captured.asc()).all()
        if len(all_scores) >= 1:
            latest_score = all_scores[-1]
            return latest_score
        else:
            return None

# Model for GAD7Scores. Used to store the score, emotional_score, time when the 
# questionnaire was done, etc.
class GAD7Scores(db.Model):
    __tablename__ = 'GAD7Scores'
    id = db.Column(db.Integer, primary_key = True)
    score = db.Column(db.Integer, nullable = False)
    emotional_state = db.Column(db.Integer, nullable = False)
    time_captured = db.Column(db.DateTime(timezone=True), default=func.now())
    patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))

    @staticmethod 
    def get_all_scores(patient_id):
        return GAD7Scores.query.filter_by(patient_id = patient_id).order_by(GAD7Scores.time_captured.asc()).all()
        
    @staticmethod 
    def get_latest_score(patient_id):
        all_scores = GAD7Scores.query.filter_by(patient_id = patient_id).order_by(GAD7Scores.time_captured.asc()).all()
        if len(all_scores) >= 1:
            latest_score = all_scores[-1]
            return latest_score
        else:
            return None

# Base user model, used in order to define the base attributes both the
# therapist and patient should have. These attributes include the names.
# email, password, etc.
class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(150))
    type = db.Column(db.String(20))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    def is_patient(self):
        return self.type == 'patient'

    def is_therapist(self):
        return self.type == 'therapist'

# Model for therapist user. Has a patients attribute which corresponds 
# to the patients that the therpaist currently is associated with
class Therapist(User):
    __tablename__ = 'Therapist'
    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)

    therapy_sessions = db.relationship('SessionData')
    patients = db.relationship('Association', foreign_keys=[Association.therapist_id], backref='therapist')

    __mapper_args__ = {
        'polymorphic_identity': 'therapist',
    }

    @staticmethod
    def get_all_therapists():
        all_therapists = Therapist.query.all()
        
        return all_therapists
    
    @staticmethod
    def get_therapist(therapist_id):
        therapist = Therapist.query.get(therapist_id)
        return therapist
        
# Model for the patient user. Has various attributes corresponding to mental 
# health data, such as session_data and self-questionnaire scores. ALso has a
# therapist relationship which corresponds to the therapist the patient is 
# associated with, via the association table
class Patient(User):
    __tablename__ = 'Patient'
    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key = True)

    phq9_data = db.relationship('PHQ9Scores')
    gad7_data = db.relationship('GAD7Scores')

    session_data = db.relationship('SessionData')
    current_therapist = db.relationship('Association', foreign_keys=[Association.patient_id], backref='patient', uselist=False)

    __mapper_args__ = {
        'polymorphic_identity': 'patient',
    }

    @staticmethod
    def get_patient(patient_id):
        patient = Patient.query.get(patient_id)
        return patient
    

    