from flask import render_template, request
from flask_login import current_user
import numpy as np

from app.main import bp
from app.models import Therapist, Patient, Association

from app.utils.image_utility import preprocess_image, predict_emotions

image_list = np.zeros((1, 48, 48, 1))

@bp.route('/therapy_page', methods=['GET'])
def therapy_page():
    therapist_list = Therapist.get_all_therapists()

    if Association.query.filter_by(patient_id = current_user.id).first():
        therapist_relationship = Association.query.filter_by(patient_id = current_user.id).first()
        therapist = Therapist.query.filter_by(id = therapist_relationship.therapist_id).first()
        therapist = therapist.first_name + " " + therapist.surname
    else: 
        therapist = None

    return render_template('therapy/therapy.html', name=current_user.first_name, therapist = therapist, therapist_list = therapist_list)

@bp.route('/get_therapy_image')
def get_therapy_image():
    if request.method == 'POST':
        global image_list
        image = request.files.get('snap').read()
        if image:
            image = preprocess_image(image)
            image_list = np.concatenate((image_list, image), axis = 0)
            return ("Image captured", 200)
        else:
            return "Could not capture image."

@bp.route('/predict_therapy_images')
def predict_therapy_images():
    global image_list
    
    emotions_count, emotions_labels = predict_emotions(image_list)
    image_list = np.zeroes(1, 48, 48, 1)

    return emotions_count, emotions_labels

@bp.route('/clear_therapy_images')
def clear_therapy_images():
    global image_list
    image_list = np.zeros((1, 48, 48, 1))
    return ("Questionnaire image list cleared", 200)