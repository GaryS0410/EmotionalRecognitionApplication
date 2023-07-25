import json

def get_therapy_message(emotional_state):
    with open('app/static/json/therapy_messages/therapy_emotional_score_messages.json', 'r') as i:
        emotional_state_messages = json.load(i)
    
    message = emotional_state_messages.get(emotional_state, {}).get('message', None)
    return message

def get_questionnaire_message(emotional_state):
    with open('app/static/json/questionnaire_messages/questionnaire_emotional_score_messages.json', 'r') as i:
        emotional_state_messages = json.load(i)
    
    message = emotional_state_messages.get(emotional_state, {}).get('message', None)
    return message

def get_phq_message(phq9_score):
    with open('app/static/json/questionnaire_messages/phq9_messages.json', 'r') as i:
        score_message_map = json.load(i)

    for message in score_message_map.values():
        if phq9_score in message['phq9_score_range']:
            return message['message']
        
    return 'Invalid PHQ-9 Score Given'

def get_gad_message(gad7_score):
    with open('app/static/json/questionnaire_messages/gad7_messages.json', 'r') as i:
        score_message_map = json.load(i)

    for message in score_message_map.values():
        if gad7_score in message['gad7_score_range']:
            return message['message']
    
    return 'Invalid GAD-7 Score Given'