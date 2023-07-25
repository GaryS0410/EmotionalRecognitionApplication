
# Emotional Recognition Mental Health Application

This web application was built using Flask for a 4th year honours project at Glasgow Caledonian University. The application utilises a facial expression recognition model to capture expression data during 

## Key Development Technologies 
Flask, TensorFlow, Keras, Jinja, NumPy, Pandas, SQLite, Chart.js 

## Flask Extensions
SQLAlchemy - Object relational mapper for Flask applications allowing easier interaction with teh the applciations database.

FlaskLogin - User login/registration extension which provides user session management and general user account capabilities. 

Flask-WTF - WTForms library designed for integration with Flask applications. WTForms is a form library which provides better form validation and form rendering. 

## Running the Application
In order to run the application make sure you have Python3 installed on your local machine. The following steps can then be followed to run the application.

Step 1: Initalise empty git repository in empty directory from command prompt.
```
git init
```

Step 2: Clone repository into the directory. 
```
git clone https://github.com/GaryS0410/EmotionalRecognitionApplication.git
```

Step 3: Create a Python virtua environment
```
python -m venv env 
```
Step 4: Activate the virtual environment.
``` 
env\Scripts\activate 
```
Step 5: Install the necessary project depenancies (It is highly recommended you only do this within your newly created Python virtual envionment).
```
pip install -r requirements.txt
```
Step 6: Set Flask run variable.
```
export FLASK_APP=run.py 
```
Step 7: Run the application with the following command.
``` 
flask run 
```
The application should now be usable on the localhost port 5000.
## Application Funtionality Description
The idea behind the development of the application was to utilise facial expression recognition through a users webcam alongside pre-existing psychology practices in order to provide further insights. The following points of functionality aim to describe this:
* Therapy Session Expression Recording: A user can utilise the application to record themselves during a online therapy session. Once the user decides to end the therapy session the application will then present them with details related to the captured expressions during the session.
* Mental Health Questionnaires: The application allows users to take mental health questionniares, such as PHQ-9 and GAD-7. These questionnaires have been utilised for years in order to screen for both depressive and anxiety disorders. When the user is taking the questionnaires the application will take pictures from the users webcam in order to provide information related to the captured expressions at the end of the questionnaire, alongside the questionnaire score itself.
* Emotional Metric: The applciation is capable of utilising the captured emotions in order to classify the users emotional state using an emotional metric. The application is capable of classifying a users emotional state into either negative, neutral, or positive with positive and negative both having different severities.
* User System: The application allows a user to register an account of either a patient or therapist type. The patient user is capable of utilising the application for therapy session recording, conducting mental health questionnaires, and looking back at their saved data. The therapist user is capable of viewing the previously saved data of patients which have been assigned to them within the application in order to draw further insights from the data.
* User Dashboards: User dashboards for both the patient user and therapist user exist allowing them to easily view the saved data. The dashboards represent this data using data tables, visualisations, and other methods. 