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

@bp.route('/register_patient', methods=['GET', 'POST'])
def register_patient():
    form = RegisterPatientForm()

    if form.validate_on_submit():
        patient = Patient.query.filter_by(email = form.email.data).first()

        if patient:
            flash('An account already exists with this email. Please choose another email before registering.', category='error')
        else:

            new_patient_account = Patient(first_name = form.first_name.data, surname = form.surname.data, email = form.email.data,
                                password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()))
            db.session.add(new_patient_account)
            db.session.commit()

            # Where associations would go 
            login_user(new_patient_account, remember=True)
            flash('Account created!', category='success')
            # Re-direct to appropriate page here
            return redirect(url_for('main.profile_page'))
    return render_template('auth/register_patient.html', form=form)