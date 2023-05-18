from flask import render_template, request, flash, redirect, url_for
from app.models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
import bcrypt

from app.auth import bp 
from app.auth.forms import *

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user:
            if bcrypt.checkpw(form.password.data.encode('utf-8'), user.password):
                flash('Logged in successfully!', category = 'success')
                login_user(user, remember = True)
                return redirect(url_for('main.profile_page'))
            else:
                flash('Account does not exist. Please register an account before logging in.', category='error')
    return render_template('auth/login.html', form = form)

@bp.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@bp.route('/register_user', methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()

    if form.validate_on_submit():

        if form.account_type.data == '1':
            register_patient(form.first_name.data, form.surname.data, form.email.data, form.password.data)
            return redirect(url_for('main.profile_page'))
        elif form.account_type.data == '2':
            register_therapist(form.first_name.data, form.surname.data, form.email.data, form.password.data)
            return redirect(url_for('therapist.therapist_dash'))
    return render_template('auth/register_patient.html', form=form)


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