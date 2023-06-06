class PatientProfileData:
    def __init__(self, patient, therapist, all_sessions, most_recent_session, most_recent_session_emotions, most_recent_phq, most_recent_gad):
        self.patient = patient
        self.therapist = therapist
        self.all_sessions = all_sessions
        self.most_recent_session = most_recent_session
        self.most_recent_session_emotions = most_recent_session_emotions
        self.most_recent_phq = most_recent_phq
        self.most_recent_gad = most_recent_gad