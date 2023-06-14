import cv2
from PIL import Image
import numpy as np

from app.utils.image_utility import *

def test_preprocess_image():
    with open("./test_images/happy/happy_man_1.jpg", "rb") as file:
        sample_image = file.read()

    processed_image = preprocess_image(sample_image)

    assert isinstance(processed_image, np.ndarray)
    assert processed_image.shape == (1, 48, 48, 1)
    assert processed_image.dtype == np.float32

def test_prediction_happy():
    with open("./test_images/happy/happy_man_1.jpg", "rb") as file:
        happy_image = file.read()

    processed_image = preprocess_image(happy_image)
    image_list = [processed_image]

    emotions_count = predict_emotions(image_list, is_therapy = False)

    assert isinstance(emotions_count, dict)
    assert "happy" in emotions_count
    assert emotions_count["happy"] == 1