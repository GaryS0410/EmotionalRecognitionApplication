from app.models import User
from app.auth.forms import RegisterForm
from pytest_mock import mocker
from flask import url_for

# def test_register_patient(client, app):
#     data = {
#         "first_name": "Gary",
#         "surname": "Smith",
#         "email": "garyjsmith0410@gmail.com",
#         "password": "HelloWorld",
#         "account_type": 1
#     }

#     response = client.post('/register_user', data=data)

#     with app.app_context():
#         assert User.query.count() == 1

# def test_register_patient(client, app):

#     response = client.post("/register_user", data={
#         "first_name": "Gary",
#         "surname": "Smith",
#         "password": "helloworld",
#         "confirm_password": "helloworld",
#         "account_type": 1
#         })

#     with app.app_context():
#         assert response.status_code == 200
#         assert User.query.count() == 1