import cv2 
from tensorflow.keras.models import load_model
from PIL import Image
from io import BytesIO
import numpy as np

from app.utils import bp 

# PRE-PROCESSING A CAPTURED IMAGE
def preprocess_image(webcam_image):
    face_classifier = cv2.CascadeClassifier('app\static\ml_models\haarcascade_frontalface_default.xml')

    webcam_image = Image.open(BytesIO(webcam_image))
    grey_image = cv2.cvtColor(np.array(webcam_image), cv2.COLOR_BGR2GRAY)

    try: 
        face = face_classifier.detectMultiScale(grey_image, scaleFactor=1.3, minNeighbors=5)

        x, y, w, h = face[0]

        face_image = grey_image[y:y+h, x:x+w]

        face_image = cv2.resize(face_image, (48, 48))
        face_image = face_image.astype('float32')
        face_image /= 255.0

        face_image = np.expand_dims(face_image, axis = 0)
        face_image = np.expand_dims(face_image, axis = -1)

        return face_image
    except:
        grey_image = cv2.resize(grey_image, (48, 48))
        grey_image = grey_image.astype('float32')
        grey_image /= 255.0

        grey_image = np.expand_dims(grey_image, axis = 0)
        grey_image = np.expand_dims(grey_image, axis = -1)

        return grey_image
    
# PREDICTING ON IMAGES FUNCTIONS
def predict_emotions(image_list):
    model = load_model('app\static\ml_models\model.h5')

    image_list = np.array(image_list)

    predictions = model.predict(image_list)
    predicted_classes = np.argmax(predictions, axis =1)

    emotion_types = np.array(['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral'])
    emotion_labels = emotion_types[predicted_classes]

    emotion_types = emotion_types.tolist()
    emotion_labels = emotion_labels.tolist()

    emotions_count = {}
    for i in emotion_labels:
        if i in emotions_count:
            emotions_count[i] += 1
        else:
            emotions_count[i] = 1
    
    return emotions_count, emotion_labels