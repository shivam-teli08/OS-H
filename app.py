from flask import Flask
import os
from datetime import timedelta 
from dotenv import load_dotenv
from routes.indexRoute import indexRoute
from routes.oauthRoute import oauthRoute_bp
from routes.dashBoardRoute import dashBoardRoutebp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
app.permanent_session_lifetime=timedelta(days=7)
app.secret_key=os.getenv("SECRET_KEY")
if not app.secret_key:
    raise RuntimeError("SECRET_KEY is missing. Add SECRET_KEY to .env before starting the app.")

app.register_blueprint(indexRoute)
app.register_blueprint(oauthRoute_bp)
app.register_blueprint(dashBoardRoutebp)

