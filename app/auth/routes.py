from flask import render_template, flash, redirect, url_for
from app.models import *
from flask_login import login_user, logout_user, login_required
import bcrypt

from app.models import *

from app.auth import bp
from app.auth.forms import *
from app.auth.helpers import *

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user:
            if bcrypt.checkpw(form.password.data.encode('utf-8'), user.password):
                flash('Logged in successfully!', category = 'success')
                login_user(user, remember = True)
                if user.type == "patient":
                    return redirect(url_for('main.profile_page', patient_id = current_user.id))
                elif user.type == "therapist":
                    return redirect(url_for('therapist.therapist_dash', therapist_id = current_user.id))
            else:
                flash('Incorrect password. Please try again.', category='error')
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
            if current_user.is_authenticated:
                return redirect(url_for('main.profile_page', patient_id = current_user.id))
        elif form.account_type.data == '2':
            register_therapist(form.first_name.data, form.surname.data, form.email.data, form.password.data)
            if current_user.is_authenticated:
                return redirect(url_for('therapist.therapist_dash', therapist_id = current_user.id))
    return render_template('auth/register.html', form=form)

@bp.route('/update_details', methods = ['GET', 'POST'])
def update_details():
    form = UpdateForm()
    user = User.query.filter_by(id = current_user.id).first()

    if form.validate_on_submit():
        update_user_details(form.first_name.data, form.surname.data, form.email.data, form.password.data)
        flash('User details successfully updated.')
        if user.is_patient():
            return redirect(url_for('main.profile_page', patient_id = current_user.id))
        elif user.is_therapist():
            return redirect(url_for('therapist.therapist_dash', therapist_id = current_user.id))

    return render_template('auth/update_details.html', form = form)