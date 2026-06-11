from flask import Flask
from routes.indexRoute import indexRoute
from routes.checkRoute import check_bp  
from routes.oauthRoute import oauthRoute_bp
app = Flask(__name__)
app.register_blueprint(indexRoute)

app.register_blueprint(check_bp)
app.register_blueprint(oauthRoute_bp)

