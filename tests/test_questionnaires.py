from app.main.forms import PHQ9Form, GAD7Form

def test_phq_score(app):
    with app.app_context():
        questionnaire_answers = {
            'question1': '0',
            'question2': '1',
            'question3': '4',
            'question4': '1',
            'question5': '0',
            'question6': '0',
            'question7': '0',
            'question8': '0',
            'question9': '0'
        }

        form = PHQ9Form(data = questionnaire_answers)

        assert form.calculate_score() == 6

def test_gad_score(app):
    with app.app_context():
        questionnaire_answers = {
            'question1': '0',
            'question2': '0',
            'question3': '0',
            'question4': '0',
            'question5': '0',
            'question6': '0',
            'question7': '0'
        }

        form = GAD7Form(data = questionnaire_answers)

        assert form.calculate_score() == 0