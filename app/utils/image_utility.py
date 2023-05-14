import cv2 
from tensorflow.keras.models import load_model
from PIL import Image

from app.utils import bp 

# Pre-processing image function
def preprocess_image(image):
    face_classifier = cv2.CascadeClassifier('app\static\ml_models\haarcascade_frontalface_default.xml')
    return None

# Predicting on images function