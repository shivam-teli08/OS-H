from flask import Flask
import os
from datetime import timedelta 
from dotenv import load_dotenv
from extensions import db


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.permanent_session_lifetime = timedelta(days=7)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

from routes.indexRoute import indexRoute
from routes.oauthRoute import oauthRoute_bp
from routes.dashBoardRoute import dashBoardRoutebp
from routes.onBoardingRoute import onBoardingRoutebp
from routes.repo import repo_bp

app.register_blueprint(indexRoute)
app.register_blueprint(oauthRoute_bp)
app.register_blueprint(dashBoardRoutebp)
app.register_blueprint(onBoardingRoutebp)
app.register_blueprint(repo_bp)