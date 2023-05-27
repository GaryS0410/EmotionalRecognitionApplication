from flask import render_template, request
from flask_login import current_user
import numpy as np
# import datetime
from datetime import datetime

from app import db
from app.main import bp
from app.main.helpers import save_therapy_data

from app.models import Therapist, Patient, Association

from app.utils.image_utility import preprocess_image, predict_emotions

image_list = np.zeros((1, 48, 48, 1))
image_timestamps = []

@bp.route('/therapy_page', methods=['GET'])
def therapy_page():
    if Association.query.filter_by(patient_id = current_user.id).first():
        therapist_relationship = Association.query.filter_by(patient_id = current_user.id).first()
        therapist = Therapist.query.filter_by(id = therapist_relationship.therapist_id).first()
        therapist = therapist.first_name + " " + therapist.surname
    else: 
        therapist = None

    return render_template('therapy/therapy_screen.html', name=current_user.first_name, therapist = therapist)

@bp.route('/therapy_results_page', methods = ['GET', 'POST'])
def therapy_results_page():
    global image_list
    global image_timestamps

    is_therapy = True

    emotions_pairs, all_emotions = predict_emotions(image_list, is_therapy)

    emotional_state = "Extremely Positive"

    patient_id = current_user.id
    therapist_id = current_user.current_therapist.id

    save_therapy_data(emotional_state, patient_id, therapist_id, all_emotions, image_timestamps)

    return render_template('therapy/therapy_results.html', emotions = emotions_pairs)

@bp.route('/get_therapy_image', methods = ['POST'])
def get_therapy_image():
    global image_list
    global image_timestamps

    if request.method == 'POST':
        image = request.files.get('snap').read()
        if image:
            image = preprocess_image(image)
            image_list = np.concatenate((image_list, image), axis = 0)
            current_time = datetime.now()
            image_timestamps.append(current_time)
            return ("Image captured", 200)
        else:
            return "Could not capture image."

@bp.route('/clear_therapy_images')
def clear_therapy_images():
    global image_list
    global image_timestamps

    image_list = np.zeros((1, 48, 48, 1))
    image_timestamps = []

    return ("Questionnaire image list cleared", 200)