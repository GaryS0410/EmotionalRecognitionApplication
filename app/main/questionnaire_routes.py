from flask import render_template, request, flash
from flask_login import login_required, current_user
import numpy as np

from app import db
from app.main import bp
from app.main.forms import *
from app.main.helpers import save_questionnaire_data, determine_emotional_state, categorise_emotional_state
from app.models import PHQ9Scores, Patient

from app.utils.general_utility import *
from app.utils.image_utility import preprocess_image, predict_emotions

image_list = np.zeros((1, 48, 48, 1))

# Main Questionnaire Page

@bp.route('/questionnaires_page', methods = ['GET'])
@login_required
def questionnaires_page():
    patient = Patient.get_patient(current_user.id)
    if patient.current_therapist:
        therapist = patient.current_therapist.therapist
    else:
        flash('You do not currnetly have an assigned therapist . Please select a therapist from your profile before attempting a questionnaire.', category='error')
        therapist = None

    return render_template('/questionnaires/questionnaires_page.html', therapist = therapist)

# Routes for displaying either questionnaire

@bp.route('/phq9_questionnaire', methods = ['GET', 'POST'])
@login_required
def phq9_questionnaire():
    form = PHQ9Form()

    if form.validate_on_submit():
        score = form.calculate_score()
        
        emotions = predict_questionnaire_images()
        emotional_state = determine_emotional_state(emotions)
        
        save_questionnaire_data("PHQ", score, emotional_state, current_user.id)
        
        emotional_state = categorise_emotional_state(emotional_state)
        phq_message = get_phq_message(score)
        emotional_state_message = get_questionnaire_message(emotional_state)
        score = str(score)

        return render_template('/questionnaires/PHQ9.html', score = score, emotions = emotions, emotional_state = emotional_state, 
                               phq_message = phq_message, emotional_state_message = emotional_state_message)
    return render_template('/questionnaires/PHQ9.html', form = form)

@bp.route('/gad7_questionnaire', methods = ['GET', 'POST'])
@login_required
def gad7_questionnaire():
    form = GAD7Form()

    if form.validate_on_submit():
        score = form.calculate_score()

        emotions = predict_questionnaire_images()
        emotional_state = determine_emotional_state(emotions)
        save_questionnaire_data("GAD", score, emotional_state, current_user.id)

        emotional_state = categorise_emotional_state(emotional_state)

        gad_message = get_gad_message(score)
        emotional_state_message = get_questionnaire_message(emotional_state)

        return render_template('/questionnaires/GAD7.html', score = score, emotions = emotions, emotional_state = emotional_state, gad_message = gad_message,
                               emotional_state_message = emotional_state_message)
    return render_template('/questionnaires/GAD7.html', form = form)

# Route for clearing the global image list

@bp.route('/clear_questionnaire_images')
def clear_questionnaire_images():
    global image_list
    image_list = np.zeros((1, 48, 48, 1))
    return ("Questionnaire image list cleared", 200)

# Route for predicting on the images
@bp.route('/get_questionnaire_image', methods = ['POST'])
def get_questionnaire_image():
    if request.method == 'POST':
        global image_list
        image = request.files.get('snap').read()
        if image:
            image = preprocess_image(image)
            image_list = np.concatenate((image_list, image), axis = 0)
            return ("Image captured", 200)
        else:
            return "Could not capture image."
        
# Route for predicting on questionnaire images
def predict_questionnaire_images():
    global image_list
    is_therapy = False

    captured_emotions = predict_emotions(image_list, is_therapy)
    image_list = np.zeros((1, 48, 48, 1))

    return captured_emotions