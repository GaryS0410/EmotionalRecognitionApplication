from flask import render_template, request
from flask_login import current_user
import numpy as np
import datetime

from app.main import bp
from app.main.helpers import save_therapy_data

from app.models import Therapist, Patient, Association

from app.utils.image_utility import preprocess_image, predict_emotions

image_list = np.zeros((1, 48, 48, 1))
image_timestamps = []

@bp.route('/therapy_page', methods=['GET'])
def therapy_page():
    therapist_list = Therapist.get_all_therapists()

    if Association.query.filter_by(patient_id = current_user.id).first():
        therapist_relationship = Association.query.filter_by(patient_id = current_user.id).first()
        therapist = Therapist.query.filter_by(id = therapist_relationship.therapist_id).first()
        therapist = therapist.first_name + " " + therapist.surname
    else: 
        therapist = None

    return render_template('therapy/therapy_screen.html', name=current_user.first_name, therapist = therapist, therapist_list = therapist_list)

@bp.route('/therapy_results_page', methods = ['GET', 'POST'])
def therapy_results_page():
    global image_list
    emotions = predict_emotions(image_list)


    return render_template('therapy/therapy_results.html', emotions = emotions[0])

@bp.route('/get_therapy_image', methods = ['POST'])
def get_therapy_image():
    global image_list
    global image_timestamps

    if request.method == 'POST':
        image = request.files.get('snap').read()
        if image:
            image = preprocess_image(image)
            image_list = np.concatenate((image_list, image), axis = 0)
            current_time = datetime.datetime.now()
            print(image_timestamps)
            image_timestamps.append(current_time)
            return ("Image captured", 200)
        else:
            return "Could not capture image."

@bp.route('/predict_therapy_images')
def predict_therapy_images():
    global image_list
    global image_timestamps
    
    emotions_count, emotions_labels = predict_emotions(image_list)

    image_list = np.zeroes(1, 48, 48, 1)

    return emotions_count, emotions_labels

@bp.route('/clear_therapy_images')
def clear_therapy_images():
    global image_list
    image_list = np.zeros((1, 48, 48, 1))
    return ("Questionnaire image list cleared", 200)