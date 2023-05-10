from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), Email()])
    submit = SubmitField('Sign In')

class RegisterPatientForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    confirm_password = PasswordField('Password', validators=[DataRequired(), Length(min=7)])
    submit = SubmitField('Sign Up')

class RegisterTherapistForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2)], render_kw={"placeholder": "First Name..."})
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2)], render_kw={"placeholder": "Surname..."})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email..."})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7)], render_kw={"placeholder": "Password..."})
    confirm_password = PasswordField('Password', validators=[DataRequired(), Length(min=7)], render_kw={"placeholder": "Confirm Password..."})
    submit = SubmitField('Sign Up')