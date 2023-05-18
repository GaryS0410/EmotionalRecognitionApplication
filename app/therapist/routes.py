from flask import render_template

from app.therapist import bp 

@bp.route('/therapist_dash', methods = ['GET'])
def therapist_dash():
    return render_template('therapist_user/therapist_dash.html')