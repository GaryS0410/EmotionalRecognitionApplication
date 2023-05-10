from flask import render_template

from app.main import bp

@bp.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('landing_page.html')