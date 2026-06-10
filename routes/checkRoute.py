from flask import Blueprint , render_template

check_bp = Blueprint('check',__name__)

@check_bp.route('/check')
def check():
    return render_template('check.html')