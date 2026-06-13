from flask import Blueprint, redirect, render_template, session, url_for

indexRoute = Blueprint('indexRoute', __name__)


@indexRoute.route('/')
def index():
    if session.get("github_id") and session.get("username"):
        return redirect(url_for("dashBoardRoute.dashboard"))
    return render_template('index.html')
