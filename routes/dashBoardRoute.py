from flask import Blueprint,render_template
from middlewares.authMiddleware import login_check 
dashBoardRoutebp = Blueprint('dashBoardRoute', __name__)
@dashBoardRoutebp.route('/dashboard')
@login_check
def dashboard():
    return render_template('dashboard.html')
