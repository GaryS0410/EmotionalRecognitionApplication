from flask import render_template, request
from flask_login import login_required
import numpy as np

from app.main import bp
from app.main.forms import *

from app.utils.image_utility import preprocess_image, predict_emotions

image_list = np.zeros((1, 48, 48, 1))

# Main Questionnaire Page

@bp.route('/questionnaires_page', methods = ['GET'])
@login_required
def questionnaires_page():
    return render_template('questionnaires_page.html')

# Routes for displaying either questionnaire

@bp.route('/phq9_questionnaire', methods = ['GET', 'POST'])
@login_required
def phq9_questionnaire():
    form = PHQ9Form()

    if form.validate_on_submit():
        score = form.calculate_score()
        
        emotions = predict_questionnaire_images()
        print(emotions)
        print(score)

        return render_template('/questionnaires/PHQ9.html', score = score)
    return render_template('/questionnaires/PHQ9.html', form = form)

@bp.route('/gad7_questionnaire', methods = ['GET', 'POST'])
@login_required
def gad7_questionnaire():
    form = GAD7Form()

    if form.validate_on_submit():
        score = form.calculate_score()

        return render_template('/questionnaires/GAD7.html', score = score)
    return render_template('/questionnaires/GAD7.html', form = form)

# Route for clearing the global image list 

@bp.route('/clear_questionnaire_images')
def clear_questionnaire_images():
    global image_list
    image_list = np.zeros((1, 48, 48, 1))
    return 200

# Route for predicting on the images
@bp.route('/get_questionnaire_image', methods = ['POST'])
def get_questionnaire_image():
    if request.method == 'POST':
        global image_list
        image = request.files.get('snap').read()
        if image:
            image = preprocess_image(image)
            image_list = np.concatenate((image_list, image), axis = 0)
            return 200
        else:
            return "Could not capture image."
        
# Route for predicting on questionnaire images
@bp.route('/predict_questionnaire_images', methods = ['GET'])
def predict_questionnaire_images():
    global image_list

    captured_emotions = predict_emotions(image_list)
    image_list = np.zeros((1, 48, 48, 1))

    return captured_emotions