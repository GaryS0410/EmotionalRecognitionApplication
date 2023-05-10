from flask import render_template
from app.errors import bp 

@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'), 500

@bp.app_errorhandler(401)
def authorisation_error(e):
    return render_template('errors/401.html'), 401