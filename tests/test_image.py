import cv2
from PIL import Image
import numpy as np

from app.utils.image_utility import preprocess_image

def test_preprocessing():
    # './test_images/happy_man_1.jpg'
    # tests\test_images\happy_man_1.jpg
    sample_image_path = 'tests/test_images/happy_man_1.jpg'
    with open(sample_image_path, 'rb') as f:
        sample_image_bytes = f.read()

    face_result = np.array([[10, 10, 20, 20]])

    class MockCascadeClassifier:
        def detectMultiScale(self, image, scaleFator, minNeighbors):
            return face_result
        
    original_classifier = cv2.CascadeClassifier
    cv2.CascadeClassifier = MockCascadeClassifier

    result = preprocess_image(sample_image_bytes)

    cv2.CascadeClassifier.original_classifier

    assert isinstance(result, np.ndarray)
    assert result.shape == (1, 48, 48, 1)
    assert result.dtype == np.float32
    assert np.allclose(result, np.zeros((1, 48, 48, 1)))

    face_result = ()
    result = preprocess_image(sample_image_bytes)
    assert result.shape == (1, 48, 48, 1)
    assert result.dtype == np.float32
    assert np.allclose(result, np.zeros((1, 48, 48, 1)))