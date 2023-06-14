from flask import url_for, request
from flask_login import current_user
from pytest_mock import mocker

from app.models import User

def test_patient_registration(app, client):
    data = {
        "first_name": "John",
        "surname": "Doe",
        "email": "JohnDoe@gmail.com",
        "password": "helloworld",
        "confirm_password": "helloworld",
        "account_type": "1"
    }

    response = client.post('/register_user', data = data, follow_redirects = True)

    with app.app_context():
        assert User.query.filter_by(email = "JohnDoe@gmail.com").first()
        patient = User.query.filter_by(email = "JohnDoe@gmail.com").first()
        assert patient.type == "patient"

def test_therapist_registration(app, client):
    data = {
        "first_name": "Jenny",
        "surname": "Jones",
        "email": "JennyJones@gmail.com",
        "password": "worldhello",
        "confirm_password": "worldhello",
        "account_type": "2"
    }

    response = client.post('/register_user', data = data)

    with app.app_context():
        assert User.query.filter_by(email = "JennyJones@gmail.com").first()
        therapist = User.query.filter_by(email = "JennyJones@gmail.com").first()
        assert therapist.type == "therapist"

def test_patient_login(app, client):
    data = {
        "email": "JohnDoe@gmail.com",
        "password": "helloworld"
    }

    response = client.post('/login', data = data)

    with app.app_context():
        assert response.status_code == 302
        assert b"Patient Information" in response.data
 
def test_therapist_registration(app, client):
    data = {
        "first_name": "Jenny",
        "surname": "Jones",
        "email": "JennyJones@gmail.com",
        "password": "worldhello",
        "confirm_password": "worldhello",
        "account_type": "2"
    }

    response = client.post('/register_user', data = data)

    with app.app_context():
        assert User.query.filter_by(email = "JennyJones@gmail.com").first()
        therapist = User.query.filter_by(email = "JennyJones@gmail.com").first()
        assert therapist.type == "therapist"

def test_therapist_login(app, client):
    data = {
        "email": "JennyJones@gmail.com",
        "password": "helloworld"
    }

    response = client.post('/login', data = data)

    with app.app_context():
        assert response.status_code == 200