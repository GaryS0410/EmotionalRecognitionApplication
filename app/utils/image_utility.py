import cv2 
from tensorflow.keras.models import load_model
from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt

from app.utils import bp 

def crop_face(image):
    face_classifier = cv2.CascadeClassifier('app\static\ml_models\haarcascade_frontalface_default.xml')
    try:
        face = face_classifier.detectMultiScale(image, scaleFactor = 1.3, minNeighbors = 5)
        x, y, w, h = face[0]
        image = image[y:y+h, x:x+w]
        return image
    except:
        return image

def preprocess_image(image):
    image = Image.open(BytesIO(image))

    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    image = crop_face(image)
    image = cv2.resize(image, (48, 48))
    
    image = image.astype('float32')
    image /= 255.0

    image = np.expand_dims(image, axis = 0)
    image = np.expand_dims(image, axis = -1)

    return image
    
# PREDICTING ON IMAGES FUNCTIONS
def predict_emotions(image_list, is_therapy):
    # model = load_model('app\static\ml_models\model.h5')
    model = load_model('app\static\ml_models\\final_model.h5')

    if is_therapy:
        image_list = image_list[1:]

    predictions = model.predict(image_list)
    predicted_classes = np.argmax(predictions, axis = 1)

    emotion_types = np.array(['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral'])
    emotion_labels = emotion_types[predicted_classes]

    emotion_labels = emotion_labels.tolist()

    emotions_count = {}
    for i in emotion_labels:
        if i in emotions_count:
            emotions_count[i] += 1
        else:
            emotions_count[i] = 1

    if is_therapy:
        return(emotions_count, emotion_labels)
    else:
        return(emotions_count)