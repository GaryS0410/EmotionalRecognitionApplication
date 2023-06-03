from flask import url_for, request
from flask_login import current_user
from pytest_mock import mocker

from app.models import User

def test_patient_registration(app, client):
    data = {
        "first_name": "Logan",
        "surname": "Roy",
        "email": "LoganRoy@gmail.com",
        "password": "helloworld",
        "confirm_password": "helloworld",
        "account_type": "1"
    }

    response = client.post('/register_user', data = data)

    with app.app_context():
        assert User.query.filter_by(email = "LoganRoy@gmail.com").first()
        patient = User.query.filter_by(email = "LoganRoy@gmail.com").first()
        assert patient.type == "patient"

def test_patient_login(app, client):
    response = client.post('login', data = {
        "email": "LoganRoy@gmail.com",
        "password": "helloworld"
    }, follow_redirects = True)

    with app.app_context():
        assert response.status_code == 200
        assert b"Patient Information" in response.data
 
def test_therapist_registration(app, client):
    data = {
        "first_name": "Shiv",
        "surname": "Roy",
        "email": "ShivRoy@gmail.com",
        "password": "helloworld",
        "confirm_password": "helloworld",
        "account_type": "2"
    }

    response = client.post('/register_user', data = data)

    with app.app_context():
        assert User.query.filter_by(email = "ShivRoy@gmail.com").first()
        therapist = User.query.filter_by(email = "ShivRoy@gmail.com").first()
        assert therapist.type == "therapist"

def test_therapist_login(app, client):
    data = {
        "email": "ShivRoy@gmail.com",
        "password": "helloworld"
    }

    response = client.post('/login', data = data)

    with app.app_context():
        assert response.status_code == 200