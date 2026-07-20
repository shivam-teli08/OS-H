from flask import Blueprint, render_template
from middlewares.authMiddleware import login_check
indexRoute = Blueprint('indexRoute', __name__)
@indexRoute.route('/')
@login_check
def index():
    return render_template('index.html')
