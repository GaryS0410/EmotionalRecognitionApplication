from flask import flash, redirect, url_for
from flask_login import current_user, login_user
import bcrypt

from app import db

from app.models import Patient, Therapist, User

def register_patient(first_name, surname, email, password):
    patient = User.query.filter_by(email = email).first()

    if patient:
        flash('A user account already exists with this email. Please choose a unique email before registering', category='error')
    else:
        new_patient_account = Patient(first_name = first_name, surname = surname, email = email, 
                                    password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))
        db.session.add(new_patient_account)
        db.session.commit()

        login_user(new_patient_account, remember=True)
        flash('New patient account created!', category='success')
        
        return redirect(url_for('main.profile_page'))

def register_therapist(first_name, surname, email, password):
    therapist = User.query.filter_by(email = email).first()

    if therapist:
        flash('A user account already exists with this email. Please use a different valid email address for your account.')
    else:
        new_therapist_account = Therapist(first_name = first_name, surname = surname, email = email,
                                          password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))
        db.session.add(new_therapist_account)
        db.session.commit()
    
        login_user(new_therapist_account, remember=True)
        flash('New therapist account created!', category='success')

        return redirect(url_for('therapist.therapist_dash'))