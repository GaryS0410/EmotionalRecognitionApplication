from app.models import Association, Patient, SessionData

def get_current_patients(therapist_id):
    current_patient_associations = Association.get_therapist_associations(therapist_id)
    if current_patient_associations is not None:
        current_patients = []
        for association in current_patient_associations:
            patient = Patient.get_patient(association.patient_id)
            current_patients.append(patient)
        patient_count = len(current_patient_associations)
        return current_patients, patient_count
    else:
        return None

def conducted_sessions_information(therapist_id):
    conducted_sessions = SessionData.get_therapist_sessions(therapist_id)
    if conducted_sessions is not None:
        conducted_session_patients = []
        for i in conducted_sessions:
            current_patient = Patient.get_patient(i.session_patient)
            conducted_session_patients.append(current_patient)
        conducted_session_data = zip(conducted_sessions, conducted_session_patients)
        return conducted_session_data
    return None